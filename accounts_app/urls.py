from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup"),
    path('<slug:slug>/', views.ProfileView.as_view(), name="profile"),
    path('accounts/edit/', views.UpdateProfileView.as_view(), name="edit_profile"),
    path('accounts/password/change/', views.ChangePasswordView.as_view(), name="change_password"),
]
