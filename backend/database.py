import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Boolean, CheckConstraint, DateTime, ForeignKey, PrimaryKeyConstraint

class Base(DeclarativeBase):
    pass

class Offices(Base):
    __tablename__ = 'offices'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), unique=True)
    
    users: Mapped[list['Users']] = relationship(back_populates='users', uselist=True)
    employees: Mapped[list['Employees']] = relationship(back_populates='employees', uselist=True)
    
class Users(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    office_id: Mapped[int] = mapped_column(Integer, ForeignKey('offices.id'))
    is_hr: Mapped[bool] = mapped_column(Boolean, nullable=False)
    login: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True)
    
    office: Mapped['Offices'] = relationship(back_populates='offices')
    
class Employees(Base):
    __tablename__ = 'employees'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    office_id: Mapped[int] = mapped_column(Integer, ForeignKey('offices.id'))
    email: Mapped[str] = mapped_column(String(50), unique=True)
    quit_chance: Mapped[int] = mapped_column(Integer, CheckConstraint('quit_chance >= 0 AND quit_chance <= 100'))
    
    office: Mapped['Offices'] = relationship(back_populates='offices')
    emailUsage: Mapped[list['EmailUsage']] = relationship(back_populates='emailUsage', uselist=True)
    
class EmailUsage(Base):
    __tablename__ = 'emailUsage'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    employee_id: Mapped[int] = mapped_column(Integer, ForeignKey('employees.id'))
    date: Mapped[datetime.datetime] = mapped_column(DateTime)
    
    employee: Mapped['Employees'] = relationship(back_populates='employees')
