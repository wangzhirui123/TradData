# -*- coding: utf-8 -*-
__author__ = 'Px'
from tornado import web,ioloop

from tornado.options import options,define,parse_command_line
import urls
from settings import settings

define('port',80,type=int,help="在这个端口上运行服务")
parse_command_line()

if __name__ == '__main__':

    app = web.Application(urls.urls,**settings)
    app.listen(options.port)
    ioloop = ioloop.IOLoop.current().start()




