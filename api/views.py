
from .serializers import VideoSerializer
from main.models import Video
from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from django.http import StreamingHttpResponse


class VideoViewSet(viewsets.ModelViewSet):
	"""
	Viewset that allows list, create, read, update and delete 
	functionality on the Video model.
	"""
	queryset = Video.objects.all()
	serializer_class = VideoSerializer
	parser_classes = FileUploadParser,

	def retrieve(self, request, *args, **kwargs):
		try:
			video = self.get_object()
			video_path = video.file.path

			def file_iterator(file_path, chunk_size=8192):
				with open(file_path, 'rb') as video_file:
					while True:
						chunk = video_file.read(chunk_size)
						if not chunk: 
							break
						yield chunk

			response = StreamingHttpResponse(file_iterator(video_path), status=200)
			response['Content-Type'] = 'video/mp4'
			return response

		except Video.DoesNotExist:
			return Response({'message':'Video object not found.'}, status=400)
