import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Boolean, CheckConstraint, DateTime, ForeignKey, PrimaryKeyConstraint

db = SQLAlchemy()

class Departaments(db.Model):
    __tablename__ = 'departaments'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100), unique=True)
    
    users: Mapped[list['Users']] = relationship(back_populates='departament', uselist=True)
    employees: Mapped[list['Employees']] = relationship(back_populates='departament', uselist=True)
    
class Users(db.Model):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    departament_id: Mapped[int] = mapped_column(Integer, ForeignKey('departaments.id'), nullable=True)
    is_super: Mapped[bool] = mapped_column(Boolean, nullable=False)
    login: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String(250), nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=True)
    session_key: Mapped[str] = mapped_column(String(250), nullable=True, unique=True)
    
    departament: Mapped['Departaments'] = relationship(back_populates='users')
    
class Employees(db.Model):
    __tablename__ = 'employees'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    departament_id: Mapped[int] = mapped_column(Integer, ForeignKey('departaments.id'), nullable=True)
    email: Mapped[str] = mapped_column(String(50), unique=True)
    quit_chance: Mapped[int] = mapped_column(Integer, CheckConstraint('quit_chance >= 0 AND quit_chance <= 100'))
    
    departament: Mapped['Departaments'] = relationship(back_populates='employees')
    emailUsage: Mapped[list['EmailUsage']] = relationship(back_populates='employee', uselist=True)
    
class EmailUsage(db.Model):
    __tablename__ = 'emailUsage'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    employee_id: Mapped[int] = mapped_column(Integer, ForeignKey('employees.id'))
    date: Mapped[datetime.datetime] = mapped_column(DateTime)
    
    employee: Mapped['Employees'] = relationship(back_populates='emailUsage')
