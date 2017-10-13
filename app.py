#!/usr/bin/env python
# coding: utf-8

from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)

@app.route('/')
async def ping(request):
    ret = {}
    ret['ip'] = request.ip[0]  # it's actually ip and port
    ret['headers'] = request.headers
    return json(ret)

@app.route('/verify_proxy')
async def verify_proxy(request):
    ip = request.ip[0]
    proxy_ip = request.args.get('proxy_ip')
    if ip != proxy_ip:
        return json({'status': 'error', 'ip': ip, 'message': 'proxy ip does not match request ip'})
    if 'x-forwarded-for' in request.headers:
        anonymous_type = 'low'
    elif 'proxy-connection' in request.headers or 'via' in request.headers:
        anonymous_type = 'middle'
    else:
        anonymous_type = 'high'
    return json({'status': 'ok', 'ip': ip, 'message': 'proxy success', 'anonymous_type': anonymous_type})


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, help="port to listen")
    parser.add_argument('--ssl', action='store_true', help='use ssl or not')
    args = parser.parse_args()
    if args.ssl:
        ssl = {'cert': './cert.pem', 'key': './key.pem'}
        app.run(host='0.0.0.0', port=args.port, ssl=ssl, debug=True)
    else:
        app.run(host='0.0.0.0', port=args.port, debug=True)

