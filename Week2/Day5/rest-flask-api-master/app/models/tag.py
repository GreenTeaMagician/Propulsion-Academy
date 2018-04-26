from database import db

todo_item_tags = db.Table(
    'todo_item_tags',
    db.Column('id', db.Boolean),
    db.Column('todo_item_id', db.Integer, db.ForeignKey('todo_item.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
)


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(255), nullable=False)
    todo_items = db.relationship('TodoItem', back_populates="tags", secondary=todo_item_tags)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }
