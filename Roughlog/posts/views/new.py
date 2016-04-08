from django.views.generic import CreateView, FormView

from posts.models import Post
from posts.forms import PostCreateForm


class NewPostCreateView(CreateView, FormView):
    model = Post
    template_name = 'posts/new.html'
    form_class = PostCreateForm
    success_url = "/"

    # 수정!
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewPostCreateView, self).form_valid(form)
