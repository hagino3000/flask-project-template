# -*- coding: utf-8 -*-

import json
import logging

from flask import Flask, request, session, render_template
from flask import redirect, url_for, make_response
from functools import wraps


app = Flask(__name__)

# Show HTML Page
@app.route('/')
def index_page():
    return render_template('index.html',
            hoge='fuga')

# Post and redirect
@app.route('/form', methods=['POST'])
def post_and_redirect():
    param_a = request.form['param_name']
    app.logger.debug(param_a)
    return redirect(url_for('/'))


@app.route('/get', methods=['GET'])
def get_something():
    return 'OK'




########################################
# For ajax
########################################
def xhr(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.is_xhr:
            res = f(*args, **kwargs)
            res.headers['X-Content-Type-Options'] = 'nosniff'
            return res
        else:
            return "(^-^)"
    return decorated_function

# XHR GET and returns html
@app.route('/xhr/getme', methods=['GET'])
@xhr
def xhr_get():
    app.logger.debug(request.args)
    res = make_response("""
    <h1>OK this is xhr get</h1>
    """)
    res.headers["Content-Type"] = "text/html"
    return res

# XHR POST with form-url-encoded and returns text
@app.route('/xhr/postme', methods=['POST'])
@xhr
def xhr_post():
    app.logger.debug(request.form)
    res = make_response("OK this is xhr post")
    res.headers["Content-Type"] = "text/plain"
    return res

# XHR POST with JSON body and returns json
@app.route('/xhr/postme_json', methods=['POST'])
@xhr
def xhr_post_json():
    app.logger.debug(request.json)
    res = make_response(json.dumps({
        status: "OK",
        msg: "OK this is xhr post"
        }))
    res.headers["Content-Type"] = "application/json"
    return res


def main():
    app.logger.setLevel(logging.DEBUG)
    app.secret_key = "secret"
    app.run(debug = True, port=8001, host='0.0.0.0')
    
if __name__ == '__main__':
    main()
