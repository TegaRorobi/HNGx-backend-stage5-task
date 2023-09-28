from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import VideoForm
from .models import Video

# Create your views here.
class VideoUploadView(View):
	def get(self, request, *args, **kwargs):
		form = VideoForm()
		return render(request, 'upload.html', context={'form':form})

	def post(self, request, *args, **kwargs):
		form = VideoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('video-list')
		return self.get(request)

class VideoListView(View):
	def get(self, request, *args, **kwargs):
		videos = Video.objects.all()
		return render(request, 'list.html', context={'videos':videos})

class VideoPlayView(View):
	def get(self, request, pk, *args, **kwargs):
		video = Video.objects.get(pk=pk)
		return render(request, 'play.html', context={'video':video})
