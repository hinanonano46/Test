from app import app, db
from flask import render_template, request, redirect, url_for
from app.models import Car_data, Info, Car_data_new
from datetime import date, timedelta, datetime
from sqlalchemy import func


@app.route('/')
def index() :
    Sdmins = Car_data_new.query.order_by(Car_data_new.Sd).limit(5).all()
    Sd1 = Car_data_new.query.filter(Car_data_new.Sd < 28).count()
    Sd2 = Car_data_new.query.filter(Car_data_new.Sd < 29, Car_data_new.Sd > 28).count()
    Sd3 = Car_data_new.query.filter(Car_data_new.Sd < 30, Car_data_new.Sd > 29).count()
    Sd4 = Car_data_new.query.filter(Car_data_new.Sd < 31, Car_data_new.Sd > 30).count()
    Sd5 = Car_data_new.query.filter(Car_data_new.Sd < 32, Car_data_new.Sd > 31).count()
    Sd6 = Car_data_new.query.filter(Car_data_new.Sd > 32).count()
    WDmins = Car_data_new.query.order_by(Car_data_new.WD).limit(5).all()
    WD1 = Car_data_new.query.filter(Car_data_new.WD < 810).count()
    WD2 = Car_data_new.query.filter(Car_data_new.WD < 820, Car_data_new.WD > 810).count()
    WD3 = Car_data_new.query.filter(Car_data_new.WD < 830, Car_data_new.WD > 820).count()
    WD4 = Car_data_new.query.filter(Car_data_new.WD > 830).count()

    today_year = date.today().year
    today_month = date.today().month

    def year() :
        if today_month == 1 :
            t_year = today_year - 1
        else :
            t_year = today_year
        return t_year

    def month() :
        if today_month == 1 :
            t_month = 12
        else :
            t_month = today_month - 1
        return t_month

    def target_avg(data_name, datemin, datemax, idmin, idmax) :
        count_Data = db.session.query(db.func.avg(data_name)).filter(
            Info.date < datemax, Info.date >= datemin, Info.metro_id >= idmin, Info.metro_id <= idmax).first()
        countData = round(count_Data[0], 2)
        return countData

    last_date_min = date(year(), month(), 1).isoformat()
    last_date_max = date(year(), month() + 1, 1).isoformat()
    compare_date_min = date(year(), month() - 1, 1).isoformat()
    compare_date_max = last_date_min
    first_stage_Sdavg = target_avg(Info.Sd_avg, last_date_min, last_date_max, '02001', '02024')
    second_stage_Sdavg = target_avg(Info.Sd_avg, last_date_min, last_date_max, '02025', '02038')
    first_stage_WDavg = target_avg(Info.WD_avg, last_date_min, last_date_max, '02001', '02024')
    second_stage_WDavg = target_avg(Info.WD_avg, last_date_min, last_date_max, '02025', '02038')
    first_stage_Sdavg_old = target_avg(Info.Sd_avg, compare_date_min, compare_date_max, '02001', '02024')
    second_stage_Sdavg_old = target_avg(Info.Sd_avg, compare_date_min, compare_date_max, '02025', '02038')
    first_stage_WDavg_old = target_avg(Info.WD_avg, compare_date_min, compare_date_max, '02001', '02024')
    second_stage_WDavg_old = target_avg(Info.WD_avg, compare_date_min, compare_date_max, '02025', '02038')
    first_stage_Sdavg_per = round(first_stage_Sdavg - first_stage_Sdavg_old, 2)
    second_stage_Sdavg_per = round(second_stage_Sdavg - second_stage_Sdavg_old, 2)
    first_stage_WDavg_per = round(first_stage_WDavg - first_stage_WDavg_old, 2)
    second_stage_WDavg_per = round(second_stage_WDavg - second_stage_WDavg_old, 2)

    return render_template('index.html', Sdmins=Sdmins, Sd1=Sd1, Sd2=Sd2, Sd3=Sd3, Sd4=Sd4, Sd5=Sd5, Sd6=Sd6,
                           WDmins=WDmins, WD1=WD1, WD2=WD2, WD3=WD3, WD4=WD4, year=year(), month=month(),
                           countSd1=first_stage_Sdavg, countSd2=second_stage_Sdavg,
                           countWD1=first_stage_WDavg, countWD2=second_stage_WDavg,
                           per1=first_stage_Sdavg_per, per2=second_stage_Sdavg_per,
                           per3=first_stage_WDavg_per, per4=second_stage_WDavg_per)


@app.route('/wheel_list')
def wheel_list() :
    page = request.args.get('page', 1, type=int)
    metro_id = request.args.get('metro_id', '', type=str)
    condition = Car_data_new.metro_id.like('%' + metro_id + '%')
    datas = Car_data_new.query.filter(condition).order_by(Car_data_new.date.desc()).paginate(page, per_page=24)
    count = Car_data_new.query.filter(condition).count()

    return render_template('wheel_list.html', datas=datas, count=count)


@app.route('/car_list')
def car_list() :
    page = request.args.get('page', 1, type=int)
    metro_id2 = request.args.get('metro_id2', '', type=str)
    condition = Info.metro_id.like('%' + metro_id2 + '%')
    datas = Info.query.filter(condition).order_by(Info.date.desc()).paginate(page, per_page=24)
    count = Info.query.filter(condition).count()
    return render_template('car_list.html', datas=datas, count=count)


@app.route('/search_Sd')
def search_Sd() :
    page = request.args.get('page', 1, type=int)
    min = request.args.get('min', 0.0, type=float)
    max = request.args.get('max', 34.0, type=float)

    datas = Car_data_new.query.filter(Car_data_new.Sd >= min, Car_data_new.Sd <= max).order_by(
        Car_data_new.Sd).paginate(page, per_page=10)
    count = Car_data_new.query.filter(Car_data_new.Sd >= min, Car_data_new.Sd <= max).count()
    return render_template('search_Sd.html', datas=datas, count=count)


@app.route('/search_WD')
def search_WD() :
    page = request.args.get('page', 1, type=int)
    min = request.args.get('min', 0.0, type=float)
    max = request.args.get('max', 1000.0, type=float)

    datas = Car_data_new.query.filter(Car_data_new.WD >= min, Car_data_new.WD <= max).order_by(
        Car_data_new.WD).paginate(page, per_page=10)
    count = Car_data_new.query.filter(Car_data_new.WD >= min, Car_data_new.WD <= max).count()
    return render_template('search_WD.html', datas=datas, count=count)


@app.route('/abration', methods=['GET', 'POST'])
def abration() :
    def car_n() :
        name = []
        for i in range(1, 10) :
            name.append(f'0200{i}')
        for i in range(10, 39) :
            name.append(f'020{i}')
        return name
    a = request.json
    print(a)
    datemin = request.args.get('datemin', '', type=str)
    datemax = request.args.get('datemax', '', type=str)
    date_mins = Info.query.filter(Info.metro_id == '02024').order_by(Info.date).all()
    date_maxs = Info.query.filter(Info.metro_id == '02024').order_by(Info.date.desc()).all()

    # datemins = db.session.query(db.func.avg(Car_data.Sd)).filter(Car_data.metro_id == '02024', Car_data.Sd >= 27,
    #                                                              Car_data.Sd <= 29,
    #                                                              Car_data.date == datemin).first()
    # datemaxs = db.session.query(db.func.avg(Car_data.Sd)).filter(Car_data.metro_id == '02024', Car_data.Sd >= 27,
    #                                                              Car_data.Sd <= 29,
    #                                                              Car_data.date == datemax).first()
    # print(datemaxs[0]-datemins[0])
    return render_template('abration.html', car_n=car_n(), date_mins=date_mins, date_maxs=date_maxs)
