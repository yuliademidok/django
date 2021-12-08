from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic

from accounts_app.models import User
from profile_app.forms import UpdateProfileForm, UpdateUserForm
from profile_app.models import Profile
from publication_app.models import Post


class ProfileView(LoginRequiredMixin, generic.DetailView):
    template_name = "profile_app/profile.html"
    model = Profile
    context_object_name = "profile"

    def __get_user_id(self):
        slug = Profile.objects.get(slug=self.kwargs.get('slug'))
        user = User.objects.get(username=slug).pk
        return user

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super(ProfileView, self).get_context_data(**kwargs)
        data["title"] = Profile.username
        data["posts"] = Post.objects.filter(user=self.__get_user_id())
        return data


class UpdateProfileView(LoginRequiredMixin, generic.UpdateView):
    template_name = "profile_app/update_profile.html"

    def get(self, request, *args, **kwargs):
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
        context = {'user_form': user_form, 'profile_form': profile_form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            user_form = UpdateUserForm(request.POST, instance=request.user)
            profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
            if profile_form.is_valid():
                profile_form.save()
                user_form.save()
                messages.success(request, 'Your profile is updated successfully')
                return redirect(to="profile:profile")
        else:
            user_form = UpdateUserForm(instance=request.user)
            profile_form = UpdateProfileForm(instance=request.user.profile)
        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})

# @login_required
# def update_profile(request):
#     template_name = "profile_app/update_profile.html"
#     if request.method == 'POST':
#         user_form = UpdateUserForm(request.POST, instance=request.user)
#         profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
#         if user_form.is_valid():
#             profile_form.save()
#             user_form.save()
#             messages.success(request, 'Your profile is updated successfully')
#             return redirect(to="profile")
#     else:
#         user_form = UpdateUserForm(instance=request.user)
#         profile_form = UpdateProfileForm(instance=request.user.profile)
#     return render(request, template_name, {'user_form': user_form, 'profile_form': profile_form})
