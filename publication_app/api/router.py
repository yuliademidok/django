from rest_framework import routers
from rest_framework.routers import Route, DynamicRoute, SimpleRouter

from publication_app.api.views.publications import PostsViewSet

api_router = routers.DefaultRouter()

api_router.register("post", PostsViewSet)


# class CustomReadOnlyRouter(SimpleRouter):
#     routes = [
#         Route(
#             url=r'^{prefix}$',
#             mapping={
#                 'get': 'list',
#                 'post': 'create',
#                 'retrieve': 'list',
#                 'put': 'update',
#                 'patch': 'partial_update',
#                 'delete': 'destroy'
#             },
#             name='{basename}-list',
#             detail=False,
#             initkwargs={'suffix': 'List'}
#         ),
#         Route(
#             url=r'^{prefix}/{lookup}$',
#             mapping={
#                 'get': 'retrieve',
#                 'put': 'update',
#                 'patch': 'partial_update',
#                 'delete': 'destroy'
#             },
#             name='{basename}-list',
#             detail=False,
#             initkwargs={'suffix': 'List'}
#         ),
#         DynamicRoute(
#             url=r'^{prefix}/{url_path}$',
#             name='{basename}-{url_name}',
#             detail=False,
#             initkwargs={}
#         )
#     ]
#
#
# api_router = CustomReadOnlyRouter()
# api_router.register("", PostsViewSet)
# urlpatterns = api_router.urls
