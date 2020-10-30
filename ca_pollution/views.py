# from django.contrib.gis.db import models
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import Context, loader
from django import template
from django.conf import settings
# from django.shortcuts import render_to_response
# from django.template import RequestContext
# from django.views.generic.simple import direct_to_template

# def my_generic_view(request, template='../templates/COPY_ca_pollution.html'):
#     return direct_to_template(request, template, context={
#         'MAPBOXAPI': os.env.get('MAPBOX_API')
#     })


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

    now = datetime.datetime.now()
    cxt = {'now': now, 'mapbox': settings.MAPBOXAPI}
    html = template.loader.get_template('ca_pollution.html').render(cxt)

    return HttpResponse(html)


