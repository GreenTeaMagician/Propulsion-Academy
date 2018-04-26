from models import Tag, TodoItem
from views.helpers import APIView


class TagListCreateView(APIView):
    methods = ['GET', 'POST']
    post_fields = ['name']

    def get(self):
        items = Tag.query.all()
        return self.make_response([l.serialize() for l in items])

    def post(self):
        data = super().post()
        name = data.get('name')
        items = Tag.query.filter_by(name=name).all()
        if items:
            return self.abort(f'Tag with the name "{name}" already exists!')
        new_item = Tag(name=name)
        self.session.add(new_item)
        self.session.commit()
        return self.make_response(new_item.serialize())


class TagGetUpdateDeleteView(APIView):
    methods = ['GET', 'POST', 'DELETE']
    post_fields = ['name']

    def get_tag(self, tag_id):
        item = Tag.query.filter_by(id=tag_id).first()
        if not item:
            return self.abort('Tag does not exist!')
        return item

    def get(self, **kwargs):
        item = self.get_tag(**kwargs)
        return self.make_response(item.serialize())

    def post(self, **kwargs):
        data = super().post()
        name = data.get('name')
        item = self.get_tag(**kwargs)
        item.name = name
        self.session.merge(item)
        self.session.commit()
        return self.make_response(item.serialize())

    def delete(self, **kwargs):
        item = self.get_tag(**kwargs)
        self.session.delete(item)
        self.session.commit()
        return f'Tag {kwargs.get("tag_id")} deleted!'


class TagSearchView(APIView):
    methods = ['GET']

    def get(self, **kwargs):
        search_string = self.request.values.get('q')
        lists = Tag.query.filter(Tag.name.like(f'%{search_string}%'))
        return self.make_response([l.serialize() for l in lists])
