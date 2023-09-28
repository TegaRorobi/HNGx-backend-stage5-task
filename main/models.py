from django.db import models
from django.urls import reverse

# Create your models here.
class Video(models.Model):
	title = models.CharField(max_length=150, null=True, blank=True)
	file = models.FileField(upload_to='videos/')
	upload_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title or self.file.url

	def get_absolute_url(self):
		return reverse('video-play', kwargs={'pk':self.id})
