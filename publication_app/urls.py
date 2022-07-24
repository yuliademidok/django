from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name = "publication"
urlpatterns = [
    path('', views.MainView.as_view(), name="main_page"),
    path('<int:pk>/', cache_page(60)(views.DetailView.as_view()), name="post_detail"),
    path('add_post/', views.PostCreateView.as_view(), name="add_post"),
    path('<int:pk>/results/', cache_page(60)(views.ResultView.as_view()), name="post_result"),
]
