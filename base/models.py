from django.db import models


class Amenitie(models.Model):
	name = models.CharField(max_length=50)
	
	def __str__(self):
		return self.name

class Hotel(models.Model):
	name = models.CharField(max_length=50)
	desc = models.TextField()
	price = models.IntegerField()
	image = models.FileField(upload_to='images')
	amenities = models.ManyToManyField(Amenitie)
	
	def __str__(self):
		return self.name
