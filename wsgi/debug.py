#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
from web import form
from web.contrib.template import render_mako

import model

urls = (
        '/', 'index',
        '/tips', 'tips',
        '/user', 'user',
        '/log', 'log',
        )
render = render_mako(
        directories=['templates'],
        input_encoding='utf-8',
        output_encoding='utf-8',
        )


application = web.application(urls, globals(), autoreload=True)
app=application.wsgifunc()

class index:
    def GET(self):
        web.header('Content-Type','text/html; charset=utf-8', unique=True)
        return render.index()

class tips:
    def GET(self):
        '''Process GET request'''
        web.header('Content-Type','application/json; charset=utf-8', unique=True)
        content = model.tips_to_json(*model.get_tips())
        return render.tip(content=content)

class user:
    def GET(self):
        '''Process GET request'''
        web.header('Content-Type','application/json; charset=utf-8', unique=True)
        content = model.userget_to_json(*model.get_user())
        return render.user(content=content)

class log:
    def GET(self):
        '''Process GET request'''
        web.header('Content-Type','application/json; charset=utf-8', unique=True)
        content = model.log_to_json(*model.get_log())
        return render.log(content=content)
        

if __name__ == "__main__":
    application.run()
