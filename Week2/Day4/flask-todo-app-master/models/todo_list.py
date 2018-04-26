from datetime import datetime

from database import db


class TodoList(db.Model):
    __tablename__ = 'todo_list'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    created = db.Column(db.DateTime, nullable=True,
                        default=datetime.utcnow)

    def serialize(self):
        datetime_format = '%Y-%m-%d %H:%M:%S'
        return {
            'id': self.id,
            'name': self.name,
            'created': self.created.strftime(datetime_format),
        }
