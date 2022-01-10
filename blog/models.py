from django.db import models
from datetime import date
# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=200)
	discription = models.TextField()
	date = models.DateField(default=date.today)
	

	def __str__(self):
		return self.title 