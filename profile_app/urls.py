from django.urls import path

from . import views

app_name = "profile"
urlpatterns = [
    path('<slug:slug>/', views.ProfileView.as_view(), name="profile"),
    path('edit/', views.UpdateProfileView.as_view(), name="update_profile"),
    # path('edit/', views.update_profile, name="update_profile"),
]
