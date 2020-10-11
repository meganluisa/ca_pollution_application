# from django.contrib.gis.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import Context, loader

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import TriRelease
# #from .serializers import TriReleaseSerializer
# from django.core.serializers import serialize 
# from django.http import JsonResponse
# import json 

# # Create your views here.

# #List all Releases
# class TriReleaseList(APIView):
#     def get(self, request):
#         tri_releases = TriRelease.objects.all()[:10]
#         serializer = serialize('geojson', tri_releases, geometry_field='geom', fields=('year', 'f', 'frs_id', 'f_lat', 'f_long', 'industry', 'pollutant', 'cas_id', 'release', 'unit', 'clean_air', 'metal', 'carcinogen', 'medium',))
#         new_tri_json = json.loads(serializer)
#         return Response(new_tri_json)

def index(request):
    return render(request, 'ca_pollution.html')