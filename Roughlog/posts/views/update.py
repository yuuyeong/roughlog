from django.views.generic.edit import UpdateView
from django.views.generic import DetailView

from posts.forms import PostUpdateForm
from posts.models import Post
from tags.models import Tag


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'posts/update.html'
    slug_field = "pk"

    def form_valid(self, form):
        tag_list = self.request.POST.get('tag_set').split(" ")
        for tag_name in tag_list:
            if tag_name is "":
                continue
            tag, is_created = Tag.objects.get_or_create(
                name=tag_name,
            )
            form.instance.tag_set.add(tag)

        return super(PostUpdateView, self).form_valid(form)
