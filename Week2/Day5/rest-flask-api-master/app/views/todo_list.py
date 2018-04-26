from models import TodoList
from views.helpers import APIView


class TodoListsListCreateView(APIView):
    methods = ['GET', 'POST']
    post_fields = ['name']

    def get(self):
        todo_lists = TodoList.query.all()
        return self.make_response([l.serialize() for l in todo_lists])

    def post(self):
        data = super().post()
        name = data.get('name')
        todo_lists = TodoList.query.filter_by(name=name).all()
        if todo_lists:
            return self.abort(f'Todo list with the name "{name}" already exists!')
        new_todo_list = TodoList(name=name)
        self.session.add(new_todo_list)
        self.session.commit()
        return self.make_response(new_todo_list.serialize())


class TodoListGetUpdateDeleteView(APIView):
    methods = ['GET', 'POST', 'DELETE']
    post_fields = ['name']

    def get_todo_list(self, todo_list_id):
        todo_list = TodoList.query.filter_by(id=todo_list_id).first()
        if not todo_list:
            return self.abort('Todolist does not exist!')
        return todo_list

    def get(self, **kwargs):
        todo_list = self.get_todo_list(**kwargs)
        return self.make_response(todo_list.serialize())

    def post(self, **kwargs):
        data = super().post()
        name = data.get('name')
        todo_list = self.get_todo_list(**kwargs)
        todo_lists = TodoList.query.filter_by(name=name).all()
        if todo_lists:
            return self.abort(f'Todo list with the name "{name}" already exists!')
        todo_list.name = name
        self.session.merge(todo_list)
        self.session.commit()
        return self.make_response(todo_list.serialize())

    def delete(self, **kwargs):
        todo_list = self.get_todo_list(**kwargs)
        self.session.delete(todo_list)
        self.session.commit()
        return f'TodoList {kwargs.get("todo_list_id")} deleted!'


class TodoListSearchView(APIView):
    methods = ['GET']

    def get(self, **kwargs):
        search_string = self.request.values.get('q')
        lists = TodoList.query.filter(TodoList.name.like(f'%{search_string}%'))
        return self.make_response([l.serialize() for l in lists])
