from rest_framework.routers import DefaultRouter
from .views import FollowViewSet, GroupViewSet, PostViewSet, CommentViewSet
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = DefaultRouter()
router.register(r'follow', FollowViewSet, basename='follow')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'posts/(?P<post_pk>\d+)/comments',
                CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('jwt/create/', TokenObtainPairView.as_view()),
    path('jwt/refresh/', TokenRefreshView.as_view()),
    path('jwt/verify/', TokenVerifyView.as_view()),
]
