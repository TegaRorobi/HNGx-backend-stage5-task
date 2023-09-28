from django.contrib import admin
from .models import Video

# Register your models here.
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
	class Meta:
		model = Video 
		list_display = 'title', 'file', 'upload_date'
