from django.db import models

# Create your models here.
class Proj(models.Model):
	title = models.CharField(max_length=100)
	discription = models.CharField(max_length=250)
	image = models.ImageField(upload_to = 'portfolio/images/')
	URL = models.URLField(blank = True)


	def __str__(self):
		return self.title 