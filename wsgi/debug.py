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
        i = web.input()
        email = i.email
        user = model.users.get_user(email)
        content = user.to_json()
        return render.user(content=content)
        
    def POST(self):
        i = web.input()
        email = str(i.email)
        model.users.user_list.append(model.User(email, int(i.cigarsPerDay), int(i.cigarsPerPacket), float(i.pricerPerPacket), str(i.stopSmokingDate)))

class log:

    def GET(self):
        '''Process GET request'''
        web.header('Content-Type','application/json; charset=utf-8', unique=True)
        content = model.log_to_json(*model.get_log())
        return render.log(content=content)
    
    def POST(self):
        i = web.input()
        userId = int(i.userId)
        is_ok = bool(i.is_ok)
        day = str(i.day)
        smokedCigars = int(i.smokedCigars)
        

if __name__ == "__main__":
    application.run()
