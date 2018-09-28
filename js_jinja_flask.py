# https://www.tutorialspoint.com/flask/flask_static_files.htm

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
   return render_template("js_jinja.html")

if __name__ == '__main__':
   app.run(debug = True)