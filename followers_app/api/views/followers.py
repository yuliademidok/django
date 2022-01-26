import itertools

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin

from followers_app.api.serializers.followers import FollowUserSerializer, FollowTagSerializer
from followers_app.models import Followers
from publication_app.api.serializers.publications import PostSerializer


class FollowUserViewSet(GenericViewSet, CreateModelMixin):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = FollowUserSerializer
    queryset = Followers.objects.all()

    @action(methods=["get"], detail=False, serializer_class=PostSerializer)
    def posts(self, request):
        instance = self.get_queryset().filter(follower_user=request.user).all()
        posts = list(itertools.chain(*[i.following_user.posts.all() for i in instance]))
        # posts = Post.objects.filter(user__in=[i.following_user.pk for i in request.user.following.all()])
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)


class UnfollowUserViewSet(GenericViewSet, DestroyModelMixin):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = FollowUserSerializer
    queryset = Followers.objects.all()


class FollowTagViewSet(GenericViewSet, CreateModelMixin):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = FollowTagSerializer
    queryset = Followers.objects.all()
