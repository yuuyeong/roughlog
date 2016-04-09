from django.contrib.auth import get_user_model
from django.views.generic import DetailView, TemplateView


class UserProfilePage(DetailView):
    model = get_user_model()
    template_name = "users/profile_my_post.html"
    slug_field = "nickname"


class UserClipPostView(TemplateView):
    template_name = "users/profile_post_clip.html"
