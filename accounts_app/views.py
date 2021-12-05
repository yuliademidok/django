from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from accounts_app.forms import LoginForm, SignUpForm
from accounts_app.models import User


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
    form = SignUpForm
    success_url = reverse_lazy('login')

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
