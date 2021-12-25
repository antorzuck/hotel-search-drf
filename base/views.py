from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import *
from base.serializers import *
from django.shortcuts import render




def home(request):
	return render(request, 'index.html')

@api_view(['GET'])
def amenities(request):
	allAmenite = Amenitie.objects.all()
	serializer = Amenites(allAmenite, many=True) 
	return Response(serializer.data)
	

@api_view(['GET'])
def hotels(request):
	allHotels = Hotel.objects.all()
	price = request.GET.get('price')
	if price:
		allHotels = allHotels.filter(price__lte=price).distinct()
	am = []
	amenites = request.GET.get('amenites')
	if amenites:
		a = amenites.split(',')
		for i in a:
			am.append(i)
		allHotels = allHotels.filter(amenities__in=am).distinct()
	serializer = Hotels(allHotels, many=True, context={'request':request})
	return Response(serializer.data)