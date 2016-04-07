from django.views.generic import ListView


class UserProfilePage(ListView):
    template_name = "users/profile.html"
    slug_field = "nickname"
