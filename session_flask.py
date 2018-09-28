# https://overiq.com/flask/0.12/sessions-in-flask/
# https://www.tutorialspoint.com/flask/flask_sessions.htm

from flask import Flask, session, redirect, url_for, request
import requests
app = Flask(__name__)
app.secret_key = 'ritu'


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
               "<b><a href = '/logout'>click here to log out</a></b>"

    return "You are not logged in <br><a href = '/login'></b>" + \
           "click here to log in</b></a>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("POST")
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action = "" method = "post">
            <p><input type = text name = username></p>
            <p><input type = submit value = Login></p>
        </form>
   '''


@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))

# update session
@app.route('/session/')
def updating_session():
    res = str(session.items())
    cart_item = {'pineapples': '10', 'apples': '20', 'mangoes': '30'}
    if 'cart_item' in session:
        session['cart_item']['pineapples'] = '100'
        session.modified = True
    else:
        session['cart_item'] = cart_item

    return res

if __name__ == '__main__':
    app.run(debug=True)
