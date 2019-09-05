# -*- coding: utf-8 -*-
__author__ = 'Px'

from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.types import Integer,String,Date,Float,Text,DateTime
from sqlalchemy.orm import sessionmaker
conn_url = 'mysql://root:123456@127.0.0.1:3306/mysql?charset=utf8'
engine = create_engine(conn_url,encoding='utf8',echo=True)
Base = declarative_base(bind=engine)

class User(Base):
    __tablename__ = 't_proxy'
    P_id = Column(Integer,primary_key=True,autoincrement=True)
    IP = Column(String(length=20))
    proxy = Column(String(length=5))
    HttpType = Column(String(length=5))
    CheckDateTime = Column(DateTime)


# Base.metadata.create_all()

def insert(ip):
    import datetime
    session = sessionmaker(bind=engine)
    conn = session()
    ip = User(IP='192.168.1.{}'.format(ip),proxy='{}'.format(ip),HttpType='http',CheckDateTime=datetime.datetime.now())
    conn.add(ip)
    conn.commit()
    conn.refresh(ip)
    conn.close()



def queryAll(t_name):
    session = sessionmaker(bind=engine)
    conn = session()
    ips = conn.query(t_name).all()
    conn.close()
    print(ips)
    return ips




