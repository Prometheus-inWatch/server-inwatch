#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
from web import form
from web.contrib.template import render_mako

import tips_helper

urls = (
        '/', 'index',
        '/tips', 'tips'
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
        web.header('Content-Type','application/json; charset=utf-8', unique=True)
        return render.index()

class tips:
    def GET(self):
        '''Process GET request'''
        web.header('Content-Type','application/json; charset=utf-8', unique=True)
        content = tips_helper.to_json(*tips_helper.get_tip())
        return render.tips(content=content)
        

if __name__ == "__main__":
    application.run()
