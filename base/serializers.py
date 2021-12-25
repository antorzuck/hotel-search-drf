from rest_framework import serializers
from .models import *

class Amenites(serializers.ModelSerializer):
	class Meta:
		model = Amenitie
		fields = '__all__'
		
class Hotels(serializers.ModelSerializer):
	amenities = Amenites(many=True, read_only=True)
	class Meta:
		model = Hotel
		exclude = ('id',)