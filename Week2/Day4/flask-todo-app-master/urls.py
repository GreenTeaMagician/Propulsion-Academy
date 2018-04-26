from flask import Blueprint

from views.tag import TagListCreateView, TagGetUpdateDeleteView, TagSearchView
from views.todo_item import TodoItemListCreateView, TodoItemGetUpdateDeleteView, TodoItemSearchView, \
    TodoItemTagFilterView
from views.todo_list import TodoListsListCreateView, TodoListGetUpdateDeleteView, TodoListSearchView

todo_list_api = Blueprint('todo-list-api', 'todo-list-api')
todo_list_api.add_url_rule(
    rule='/',
    view_func=TodoListsListCreateView.as_view('todo-lists-list-create'),
)
todo_list_api.add_url_rule(
    rule='/<int:todo_list_id>/',
    view_func=TodoListGetUpdateDeleteView.as_view('todo-lists-get-update-delete'),
)
todo_list_api.add_url_rule(
    rule='/search/',
    view_func=TodoListSearchView.as_view('todo-lists-search'),
)

todo_items_api = Blueprint('todo-item-api', 'todo-item-api')
todo_items_api.add_url_rule(
    rule='/<int:todo_list_id>/',
    view_func=TodoItemListCreateView.as_view('todo-items-list-create'),
)
todo_items_api.add_url_rule(
    rule='/<int:todo_list_id>/<int:todo_item_id>/',
    view_func=TodoItemGetUpdateDeleteView.as_view('todo-items-get-update-delete'),
)
todo_items_api.add_url_rule(
    rule='/<int:todo_list_id>/<int:todo_item_id>/filter/<int:tag_id>',
    view_func=TodoItemTagFilterView.as_view('todo-items-tag-filter'),
)
todo_items_api.add_url_rule(
    rule='/<int:todo_list_id>/search/',
    view_func=TodoItemSearchView.as_view('todo-items-search'),
)

tags_api = Blueprint('tags-api', 'tags-api')
tags_api.add_url_rule(
    rule='/',
    view_func=TagListCreateView.as_view('tags-list-create'),
)
tags_api.add_url_rule(
    rule='/<int:tag_id>/',
    view_func=TagGetUpdateDeleteView.as_view('tags-get-update-delete'),
)
tags_api.add_url_rule(
    rule='/search/',
    view_func=TagSearchView.as_view('tags-search'),
)
