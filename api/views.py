
from .serializers import VideoSerializer
from main.models import Video
from rest_framework import viewsets


class VideoViewSet(viewsets.ModelViewSet):
	"""
	Viewset that allows list, create, read, update and delete 
	functionality on the Video model.
	"""
	queryset = Video.objects.all()
	serializer_class = VideoSerializer
