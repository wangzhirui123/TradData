# -*- coding: utf-8 -*-
__author__ = 'Px'
from server import views

urls = [
    ('/',views.MainHandler),
    ('/login/?',views.LoginHandler),
    ('/agent_add/?',views.Agent_add),
    ('/proxyip/?',views.ProxyIp),
]


