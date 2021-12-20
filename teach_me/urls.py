"""teach_me URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularRedocView, SpectacularAPIView, SpectacularSwaggerView

from accounts_app.api.router import api_router as user_router
from publication_app.api.router import api_router as publication_router
from tag_app.api.router import api_router as tag_router
from likes_app.api.router import api_router as like_router
from comments_app.api.router import api_router as comment_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("publication_app.urls")),
    path("", include("accounts_app.urls")),
    path("", include("tag_app.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(),
        name="swagger-ui",
    ),
    path('users/', include(user_router.urls)),
    path('posts/', include(publication_router.urls)),
    path('tags/', include(tag_router.urls)),
    path('likes/', include(like_router.urls)),
    path('comments/', include(comment_router.urls)),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
