from rest_framework import serializers 
from main.models import Video

class VideoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Video 
		fields = 'id', 'title', 'file', 'upload_date'