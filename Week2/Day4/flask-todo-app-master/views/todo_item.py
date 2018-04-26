from datetime import datetime

from models import TodoItem, TodoList, Tag
from views.helpers import APIView


class TodoItemListCreateView(APIView):
    methods = ['GET', 'POST']
    post_fields = ['content']

    def get_todo_list(self, todo_list_id):
        todo_list = TodoList.query.filter_by(id=todo_list_id).first()
        if not todo_list:
            return self.abort('Todolist does not exist!')
        return todo_list

    def get(self, todo_list_id):
        todo_items = TodoItem.query.filter_by(todo_list_id=todo_list_id)
        return self.make_response([l.serialize() for l in todo_items])

    def post(self, **kwargs):
        data = super().post()
        todo_list = self.get_todo_list(**kwargs)
        new_todo_item = TodoItem(content=data.get('content'), todo_list=todo_list)
        self.session.add(new_todo_item)
        self.session.commit()
        return self.make_response(new_todo_item.serialize())


class TodoItemGetUpdateDeleteView(APIView):
    methods = ['GET', 'POST', 'DELETE']
    post_fields = ['content']

    def get_todo_item(self, **kwargs):
        todo_item = TodoItem.query.filter_by(id=kwargs.get("todo_item_id")).first()
        if not todo_item:
            return self.abort('TodoItem does not exist!')
        return todo_item

    def get(self, **kwargs):
        todo_item = self.get_todo_item(**kwargs)
        return self.make_response(todo_item.serialize())

    def post(self, **kwargs):
        data = super().post()
        item = self.get_todo_item(**kwargs)
        item.content = data.get('content')
        due = data.get('due')
        if due:
            try:
                due = datetime.strptime(due, self.datetime_format)
            except ValueError:
                return self.abort('Wrong DateTime format!')
            item.due = due
        done = data.get('done')
        if due:
            item.done = bool(done)
        tags = data.get('tags')
        self.session.commit()
        self.session.merge(item)
        if tags:
            tags = Tag.query.filter(Tag.id.in_(tags))
            for tag in tags:
                item.tags.append(tag)
        self.session.commit()
        return self.make_response(item.serialize())

    def delete(self, **kwargs):
        todo_item = self.get_todo_item(**kwargs)
        self.session.delete(todo_item)
        self.session.commit()
        return f'TodoItem {kwargs.get("todo_list_id")} deleted!'


class TodoItemSearchView(APIView):
    methods = ['GET']

    def get(self, todo_list_id):
        search_string = self.request.values.get('q')
        todos = TodoItem.query.filter_by(todo_list_id=todo_list_id).filter(TodoItem.content.like(f'%{search_string}%'))
        return self.make_response([l.serialize() for l in todos])


class TodoItemTagFilterView(APIView):
    methods = ['GET']

    def get_todo_list(self, todo_list_id):
        todo_list = TodoList.query.filter_by(id=todo_list_id).first()
        if not todo_list:
            return self.abort('Todolist does not exist!')
        return todo_list

    def get_tag(self, tag_id):
        item = Tag.query.filter_by(id=tag_id).first()
        if not item:
            return self.abort('Tag does not exist!')
        return item

    def get(self, **kwargs):
        todo_list = self.get_todo_list(**kwargs)
        tag = self.get_tag(**kwargs)
        todos = [i.serlaize() for i in todo_list.todos if tag in i.tags]
        return self.make_response(todos)
