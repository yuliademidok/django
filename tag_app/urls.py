from django.urls import path

from . import views

app_name = "tag"
urlpatterns = [
    path('explore/tags/<str:hashtag>/', views.HashTagView.as_view(), name="hashtag_posts"),
    path('explore/tags', views.HashTagCloudView.as_view(), name="hashtag_cloud"),
]
