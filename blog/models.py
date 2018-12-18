from django.db import models

class Post(models.Model):
	name = models.CharField(max_length=100)
	title = models.CharField(max_length=140)
	body = models.TextField()
	image = models.ImageField(upload_to='blogs', blank=True)
	date = models.DateTimeField()
	
	def __str__(self):
		return self.title

class snippet(models.Model):
	email = models.CharField(max_length=140)
	name = models.CharField(max_length=100)
	subject = models.CharField(max_length=200)
	body = models.TextField()
	
	def __str__(self):
		return self.name
