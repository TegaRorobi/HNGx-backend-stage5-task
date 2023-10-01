from django.urls import path 
from .views import VideoViewSet

urlpatterns = [
	path('upload/', VideoViewSet.as_view({'post':'create'}), name='api-video-upload'),
	path('videos/', VideoViewSet.as_view({'get':'list'}), name='api-video-list'),
	path('videos/<int:pk>/', VideoViewSet.as_view({
		'get':'retrieve', 
		'put':'update', 
		'patch':'partial_update', 
		'delete':'destroy'
		})),
]
