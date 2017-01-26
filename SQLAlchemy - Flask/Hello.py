from flask import Flask, redirect, url_for
app = Flask(__name__)

# Route for the main page
@app.route('/')
def main_page():
    return 'Hello World'

# Route for the hello world text
@app.route('/hello')
def hello_world():
    return 'hello world'

# Route for the Screen to input your tasks text
@app.route('/input-task')
def input_task():
    return 'Screen to input your tasks'

# Route for the Hello <name> text
@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'revision Numbner %f' % revNo

@app.route('/flask')
def hello_flask():
    return 'Hello Flask'

@app.route('/python/')
def hello_python():
    return 'Hello Python'

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest = name))

# app.debug = True
# app.run()
# app.run(debug = True)

if __name__ == '__main__':
    app.run(debug = True)
