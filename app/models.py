from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    login = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False, unique=True)
    code = Column(String, nullable=False, unique=True)

class UserRole(Base):
    __tablename__ = 'user_roles'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)  
    role_id = Column(Integer, ForeignKey('roles.id', ondelete='CASCADE'), nullable=False)  
    date_from = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    date_to = Column(TIMESTAMP(timezone=True), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True)

    user = relationship('User')
    role = relationship('Role')

class Foo(Base):
    __tablename__ = 'foos'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False, unique=False) 
    descritpion = Column(String, nullable=False, unique=False) 
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False) 

    user = relationship('User')

class Bar(Base):
    __tablename__ = 'bars'	

    id = Column(Integer, primary_key=True, nullable=False)
    is_active = Column(Boolean, nullable=False, server_default='TRUE')	
    foo_id = Column(Integer, ForeignKey('foos.id', ondelete='CASCADE'), nullable=False) 