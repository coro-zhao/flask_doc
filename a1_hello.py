from flask import Flask, url_for, render_template, request, redirect, abort
app = Flask(__name__)

#@app.route('/')
#def index():
#    return 'this is index'

@app.route('/user/<username>')
def show_user_profile(username):
        return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_pspst(post_id):
        return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

#@app.route('/login', methods=['GET', 'POST'])
#def login():
#	if request.method == 'POST':
#		do_the_login()
#	else:
#		show_the_login_form()

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)

#@app.route('/login', methods=['POST', 'GET'])
#def login():
#    error = None
#    if request.method == 'POST':
#        if valid_login(request.form['username'],
#                       request.form['password']):
#            return log_the_user_in(request.form['username'])
#        else:
#            error = 'Invalid username/password'
#    # the code below is executed if the request method
#    # was GET or the credentials were invalid
#    return render_template('login.html', error=error)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(200)
    this_is_never_executed()

if __name__ == '__main__':
    app.run(debug=True)
