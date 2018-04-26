from django.shortcuts import render

# Create your views here.
 from django.views.generic import TemplateView

class UserProfileView(TemplateView):
    template_name = 'user_prfile.html'

    def get_context_data(self, **kwargs):
        get_context_data(self, user_id, **kwargs)
        return context


class NewPostView(FormView):
    template_name = 'new_post.html'
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        Post.objects.create(
            user=self.request.user,
            content=form.cleaned_data.get('content')
        )
        return super().form_valid(form)