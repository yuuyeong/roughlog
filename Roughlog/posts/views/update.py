from django.views.generic.edit import UpdateView
from django.views.generic import DetailView

from posts.forms import PostUpdateForm
from posts.models import Post


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'posts/update.html'
    slug_field = "pk"
