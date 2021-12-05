from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.shortcuts import render
from django.views import generic

from accounts_app.models import User
from profile_app.models import Profile
from publication_app.models import Post


class ProfileView(LoginRequiredMixin, generic.DetailView):
    template_name = "profile_app/profile.html"
    model = Profile
    context_object_name = "profile"

    def get_user_id(self):
        slug = Profile.objects.get(slug=self.kwargs.get('slug'))
        user = User.objects.get(username=slug).pk
        return user

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super(ProfileView, self).get_context_data(**kwargs)
        data["title"] = Profile.username
        data["posts"] = Post.objects.filter(user=self.get_user_id())
        return data


class MyProfileView(ProfileView):
    template_name = "profile_app/my_profile.html"

