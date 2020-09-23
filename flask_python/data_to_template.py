# https://www.tutorialspoint.com/flask/flask_sending_form_data_to_template.htm

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print(result)
      return render_template("results.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)