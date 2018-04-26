from django.forms import ModelForm

from project.feed.models import Post

class PostForm(Form):
    content = forms.CharField(label='new post')

class PostModelForm(ModelForm):
    class Meta:
        model = Post
        fields = [content]
