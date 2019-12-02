# encoding = utf-8
# =====================================================
#   Copyright (C) 2019 All rights reserved.
#
#   filename : tornado_server.py
#   version  : 0.1
#   author   : Jack Wang / 544907049@qq.com
#   date     : 2019-12-02 下午 10:02
#   desc     : 
# =====================================================


from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from app import app  # 这里要和run.py对应

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(5000)  # flask默认的端口
IOLoop.instance().start()
