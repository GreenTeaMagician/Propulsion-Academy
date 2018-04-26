from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

'''
Initial commit (this is the commit message)

name: flask-todo-app
dependencies:
	-python-3.6
	-pip:
		-flask==0.12.1=2

'''
