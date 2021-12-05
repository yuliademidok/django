from django.urls import path

from . import views

app_name = "profile"
urlpatterns = [
    path('<slug:slug>/', views.MyProfileView.as_view(), name="my_profile"),
    path('<slug:slug>/', views.ProfileView.as_view(), name="profile"),
]
