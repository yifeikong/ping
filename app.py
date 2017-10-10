#!/usr/bin/env python
# coding: utf-8

from sanic import Sanic
from sanic.response import json

from datastore.proxy.consts import AnonymousType

app = Sanic(__name__)

@app.route('/')
async def ping(request):
    ret = {}
    ret['user_agent'] = request.headers.get('User-Agent')
    ret['ip'] = request.ip[0]  # it's actually ip and port
    # forwared is the new rfc
    ret['x_forwarded_for'] = request.headers.get('X-Forwarded-For') or request.headers.get('Forwarded')
    ret['proxy_connection'] = request.headers.get('Proxy-Connection')
    ret['via'] = request.headers.get('via')
    return json(ret)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002, debug=True)

