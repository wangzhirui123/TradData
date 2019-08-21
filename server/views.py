# -*- coding: utf-8 -*-
__author__ = 'Px'

from tornado import web,ioloop


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

        user= self.get_argument("name")
        pwd = self.get_argument("password")
        user_type = self.get_argument('sex')
        if not self.get_secure_cookie('session'):
            self.set_secure_cookie('session',"user_name:{},pwd:{},user_type:{},".format(user,pwd,user_type))
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
        pass

    def get(self, *args, **kwargs):
        self.render('pages.html')