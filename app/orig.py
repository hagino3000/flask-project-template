# -*- coding: utf-8 -*-

from flask import Flask, request, session, render_template
from flask import redirect, url_for
from functools import wraps


# Flaskのアプリケーション オブジェクトを作成
app = Flask(__name__)

# Show HTML Page
@app.route('/my')
def mypage():
    return render_template('my.html',
            time=str(time.time()),
            fuga='FUGAGF')


# Get Profile
@app.route('/profile')
def profile():
    import cProfile
    cProfile.runctx("""
            ret = 'OK'
            time.sleep(3)
            """, locals(), globals(), sort='cumulative')
    return ret

@app.route('/')
def index_html():
    import pdb;
    pdb.set_trace()
    return """
<!doctype html>
<ul>
    <li><a href="/message_form">メッセージ追加</a></li>
    <li><a href="/show">メッセージ表示</a></li>
</ul>
"""

# /message_formでアクセスされる関数
@app.route('/message_form')
def message_form():
    # テンプレートファイル templates/message_form.htmlを表示
    return render_template('message_form.html')


# /add_messageでリクエストのメッセージを登録
@app.route('/add_message', methods=['POST'])
def add_message():
    # Sessionにメッセージを登録
    import logging
    app.logger.setLevel(logging.DEBUG)
    app.logger.debug(u"デバッグメッセージ")
    app.logger.info(u"ああああああああ")
    msgs = session.get('messages', [])
    msgs.append(request.form['message'])
    session['messages'] = msgs[-10:]
    return redirect(url_for('show_messages'))


# /showでリクエストのメッセージを登録
@app.route('/show')
def show_messages():
    # テンプレートファイル templates/show_messages.htmlを表示
    return render_template('show_messages.html',
                           messages=reversed(session['messages']))




def main():
    app.secret_key = "secret"
    app.run(debug = True)
    
if __name__ == '__main__':
    main()
