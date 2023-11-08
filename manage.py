from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app, db
from app.import_data import ImportData

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('import_data', ImportData())
if __name__ == '__main__':
    manager.run()
