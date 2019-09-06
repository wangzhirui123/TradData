# -*- coding: utf-8 -*-
__author__ = 'Px'

from tornado import web
from settings import DOMAIN
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine
from server.models import ProxyIpModel






class MainHandler(web.RequestHandler):

    def initialize(self):
        pass

    async def get(self, *args, **kwargs):
        self.render('frame.html')

    def post(self, *args, **kwargs):
        pass

class LoginHandler(web.RequestHandler):

    def initialize(self):
        pass

    def get(self, *args, **kwargs):
        self.render("login.html")

    def post(self, *args, **kwargs):
        import json
        user= self.get_argument("name")
        pwd = self.get_argument("password")
        user_type = self.get_argument('sex')

        if not self.get_secure_cookie('session'):
            session_data = {
                'uname':user,
                'pwd':pwd,
                user_type:user_type
            }
            self.set_secure_cookie('session',json.dumps(session_data))
            print(self.get_secure_cookie('session'))
            self.redirect('/')
        else:
            self.redirect('/')

class Agent_add(web.RequestHandler):
    def initialize(self):
        pass

    def get(self, *args, **kwargs):

        self.render('agent_add.html')

class ProxyIp(web.RequestHandler):

    def initialize(self):
        conn_url = 'mysql://root:123456@127.0.0.1:3306/mysql?charset=utf8'
        engine = create_engine(conn_url,encoding='utf8',echo=True)
        Base = declarative_base(bind=engine)
        session = sessionmaker(bind=engine)
        self.conn = session()


    def get(self, *args, **kwargs):
        ips = self.conn.query(ProxyIpModel).order_by(ProxyIpModel.P_id.desc()).all()
        self.render('pages.html',ip_list = ips,total = len(ips))

class InterfaceIp(web.RequestHandler):

    def initialize(self):
        pass

    def get(self, *args, **kwargs):
        ApiCon = '请先生成API'
        self.render('interfaceip.html',API = ApiCon)
    def post(self, *args, **kwargs):
        import json
        uname = self.get_body_argument('loginName')
        IpNumber = self.get_body_argument('IpNumber')
        http_type = self.get_body_argument('type')
        url = DOMAIN+'/getip/?uname={}&http_type={}&IpNumber={}'.format(uname,http_type,IpNumber)
        self.render('interfaceip.html',API=url)

class GetIp(web.RequestHandler):

    def initialize(self):
        conn_url = 'mysql://root:123456@127.0.0.1:3306/mysql?charset=utf8'
        engine = create_engine(conn_url,encoding='utf8',echo=True)
        Base = declarative_base(bind=engine)
        session = sessionmaker(bind=engine)
        self.conn = session()

    def get(self, *args, **kwargs):
        IpNumber = self.get_query_argument('IpNumber')
        HttpType = self.get_query_argument('http_type')




    def post(self, *args, **kwargs):
        import json
        curr_page = int(self.get_body_argument('number'))
        size = int(self.get_body_argument('limit'))
        data_list = [{'ip':i.IP,'proxy':i.proxy,'HttpType':i.HttpType,'CheckDateTime':str(i.CheckDateTime)} for i in self.conn.query(ProxyIpModel).offset((curr_page-1)*size).limit(size).all()]
        json_data = json.dumps(data_list,ensure_ascii=False)
        self.write(json_data)





