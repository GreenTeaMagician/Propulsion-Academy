from datetime import datetime

from database import db
from models.tag import todo_item_tags


class TodoItem(db.Model):
    __tablename__ = 'todo_item'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    done = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime, nullable=True,
                        default=datetime.utcnow)
    due = db.Column(db.DateTime, nullable=True)
    todo_list_id = db.Column(
        db.Integer,
        db.ForeignKey('todo_list.id'),
        nullable=False,
    )
    todo_list = db.relationship(
        'TodoList',
        backref=db.backref('todos', lazy=True)
    )
    tags = db.relationship('Tag', back_populates="todo_items", secondary=todo_item_tags)

    def format_date(self, date):
        datetime_format = '%Y-%m-%d %H:%M:%S'
        if date:
            return date.strftime(datetime_format)
        return None

    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'done': self.done,
            'due': self.format_date(self.due),
            'created': self.format_date(self.created),
            'todo_list_id': self.todo_list_id,
            'tags': [t.serialize() for t in self.tags]
        }
