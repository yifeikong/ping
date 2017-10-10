#!/usr/bin/env python
# coding: utf-8

from sanic import Sanic
from sanic.response import json

from datastore.proxy.consts import AnonymousType

app = Sanic(__name__)

@app.route('/')
async def ping(request):
    ret = {}
    ret['ip'] = request.ip[0]  # it's actually ip and port
    ret['headers'] = request.headers
    return json(ret)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002, debug=True)

