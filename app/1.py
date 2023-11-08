a = ['TC1', 'MP1', 'M1', 'M2', 'MP2', 'TC2']
b = ['一轮', '二轮', '三轮', '四轮', '五轮', '六轮', '七轮', '八轮']


def way() :
    name=[]
    for i in range(1,10):
        name.append(f'0200{i}')
    for i in range(10,39):
        name.append(f'020{i}')

    return name


print(way())
