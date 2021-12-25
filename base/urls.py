from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('amenities/', amenities),
	path('hotels/', hotels)
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)