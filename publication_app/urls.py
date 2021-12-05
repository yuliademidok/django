from django.urls import path

from . import views

app_name = "publication"
urlpatterns = [
    path('', views.MainView.as_view(), name="main_page"),
    path('<int:pk>/', views.DetailView.as_view(), name="post_detail"),
    path('add_post/', views.PostCreateView.as_view(), name="add_post"),
    path('<int:pk>/results/', views.ResultView.as_view(), name="post_result"),
]
