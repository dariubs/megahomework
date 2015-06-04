from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname' : 'Dariush'} # fake user
	posts = [
		{
			'author' : {'nickname' : 'dap'},
			'body' : 'Beautiful day in Qazvin'
		},
		{
			'author' : {'nickname' : 'floo'},
			'body' : 'Breaking Bad was awesome!'
		}
	]
	return render_template('index.html',
							title='Home',
							user=user,
							posts=posts)
