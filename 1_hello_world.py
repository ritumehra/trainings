from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return ('Hello World')

def app_routing():
   return ('Routed using add_url_rule')

app.add_url_rule('/route','route', app_routing)

@app.route('/hello/<name>')
def hello_name(name):
   return ('Hello %s !' % name)

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

# /flask : No Error
# /flask/ : Will give error : 404

@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

# /python : No Error
# /python/ : No Error

@app.route('/python/')
def hello_python():
   return 'Hello Python'

if __name__ == '__main__':
   app.run()