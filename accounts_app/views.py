from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from accounts_app.forms import LoginForm, SignUpForm, UpdateUserForm, UpdateProfileForm
from accounts_app.models import User, Profile


class Login(LoginView):
    template_name = 'accounts_app/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True

    class Meta:
        model = User
        fields = ['username', 'password']


class Logout(LogoutView):
    template_name = 'accounts_app/login.html'


class SignUp(generic.CreateView):
    template_name = "accounts_app/signup.html"
    # success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            form = SignUpForm()
        return render(request, self.template_name, {'form': form})


class ProfileView(LoginRequiredMixin, generic.DetailView):
    template_name = "accounts_app/profile.html"
    model = Profile
    context_object_name = "profile"

    def __get_user(self):
        # return User.objects.get(username=self.kwargs.get('slug'))
        return get_object_or_404(User.objects.prefetch_related("posts"), username=self.kwargs.get('slug'))

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data["title"] = self.__get_user().username
        data["posts"] = self.__get_user().posts.all()
        return data


class UpdateProfileView(LoginRequiredMixin, generic.UpdateView):
    template_name = "accounts_app/edit_profile.html"

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
                return redirect(reverse("accounts:profile", args=[request.user]))
        else:
            user_form = UpdateUserForm(instance=request.user)
            profile_form = UpdateProfileForm(instance=request.user.profile)
        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})


class ChangePasswordView(LoginRequiredMixin, generic.UpdateView):
    template_name = "accounts_app/change_password.html"

    def get(self, request, *args, **kwargs):
        user_form = PasswordChangeForm(request.user)
        return render(request, self.template_name, {'user_form': user_form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            user_form = PasswordChangeForm(request.user, request.POST)
            if user_form.is_valid():
                user_form.save()
                return redirect("/")
        else:
            user_form = PasswordChangeForm(request.user)
        return render(request, self.template_name, {'user_form': user_form})
