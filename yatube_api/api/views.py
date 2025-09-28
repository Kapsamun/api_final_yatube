from rest_framework import viewsets, mixins, permissions, filters, status
from rest_framework.response import Response
from rest_framework.exceptions import (ValidationError, PermissionDenied,
                                       NotFound)
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import (FollowSerializer, PostSerializer,
                          CommentSerializer, GroupSerializer)
from posts.models import Follow, Post, Group
from .pagination import CustomLimitOffsetPagination
from .permissions import IsAuthorOrReadOnly
from django.shortcuts import get_object_or_404


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except ValidationError as e:
            raise e
        except Exception as e:
            raise ValidationError(f"Ошибка при создании подписки: {e}")


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly]
    pagination_class = ConditionalPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly]

    def get_queryset(self):
        try:
            post = Post.objects.get(pk=self.kwargs['post_pk'])
            return post.comments.all()
        except Post.DoesNotExist:
            raise NotFound("Пост не найден")

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        serializer.save(author=self.request.user, post=post)
