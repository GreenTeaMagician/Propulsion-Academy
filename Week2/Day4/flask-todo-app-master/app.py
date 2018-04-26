import random
import string

from flask import Flask
from flask_migrate import Migrate

from models import TodoItem
from database import db
from models.todo_list import TodoList
from urls import todo_list_api, todo_items_api, tags_api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo_app.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


migrate = Migrate(app, db)
db.init_app(app)


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


@app.cli.command()
def create_dummy_data():
    for i in range(10):
        new_list = TodoList(name=randomword(10))
        for i2 in range(10):
            new_item = TodoItem(
                content=randomword(100),
                todo_list=new_list,
            )
            db.session.add(new_item)
    db.session.commit()
    print('Created 10 Todo lists with each'
          ' 10 items!')


@app.cli.command()
def give_word():
    print(randomword(10))


app.register_blueprint(todo_list_api, url_prefix='/todo-lists')
app.register_blueprint(todo_items_api, url_prefix='/todo-items')
app.register_blueprint(tags_api, url_prefix='/tags')

if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)
