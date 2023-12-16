from sqlalchemy import Integer, Boolean, String, ForeignKey, CheckConstraint, Column, Table
from sqlalchemy.orm import relationship, declarative_base, Session
from sqlalchemy import create_engine, MetaData, select, or_, insert, update, bindparam
import configparser

config_obj = configparser.ConfigParser()
config_obj.read('backend/config.ini')
dbparam = config_obj['postgresql']

user = dbparam['user']
password = dbparam['password']
host = dbparam['host']
port = dbparam['port']
db = dbparam['database']

engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

metadata_obj = MetaData()

users_table = Table('users', metadata_obj, autoload_with=engine)
print(users_table.__dict__)

decBase = declarative_base()

class Users(decBase):
    __tablename__ = 'users'
    
    id = Column('id', Integer, primary_key=True, nullable=False)
    is_hr = Column('is_hr', Boolean)
    login = Column('login', String(30))
    password = Column('password', String(30))
    email = Column('email', String(50))
    
    employee = relationship('Employees', back_populates='user')
    
class Employees(decBase):
    __tablename__ = 'employees'
    
    id = Column('id', Integer, primary_key=True, nullable=False)
    manager_id = Column('manager_id', ForeignKey('users.id'))
    email = Column('email', String(50), nullable=False)
    quit_chance = Column('quit_chance', Integer, CheckConstraint('quit_chance >= 0 AND quit_chance <= 100'))
    
    user = relationship('Users', back_populates='employee')

statement = (
    update(Employees)
    .where(Employees.id == bindparam('id'))
    .values(email=bindparam('email'))
)

with Session(engine) as session:
    res = session.execute(
        statement,
        [
            {'id': 1, 'email': 'hello@world.com'}
        ]
    )