from django.db import models

# Create your models here.

class user(models.Model):
	firstname = models.CharField(max_length=264)

	lastname = models.CharField(max_length=264)

	email = models.EmailField(max_length=264)

	def __str__(self):
		return self.firstname