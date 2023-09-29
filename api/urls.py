from django.urls import path 
from rest_framework.routers import DefaultRouter
from .views import VideoViewSet

router = DefaultRouter()
router.register(r'videos', VideoViewSet, basename='video')

urlpatterns = router.urls