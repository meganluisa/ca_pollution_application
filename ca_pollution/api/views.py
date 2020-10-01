from django.contrib.gis.db import models
from rest_framework.response import Response
from ca_pollution.models import TriRelease, TriFacility
from rest_framework.views import APIView
#from django.core.sterializers import ModelSerializer
from django.core.serializers import serialize
import json
#from .serializer import TriReleaseSerializer
from rest_framework import generics, viewsets
from rest_framework import generics

# class TriReleaseList(generics.ListCreateAPIView):
#     model = TriRelease
#     serializer_class = TriReleaseSerializer
#     queryset = TriRelease.objects.all()[:10]

# tri_releases = TriReleaseList.as_view()


# class TriReleaseViewSet(viewsets.ModelViewSet):
#     queryset =TriRelease.objects.all()[:10]
#     serializer_class = TriReleaseSerializer

class TriReleaseList(APIView):
    def get(self, request):
        tri_releases = TriRelease.objects.all()
        #tri_releases = TriRelease.objects.all().select_related()[:30]
        serializer = serialize('geojson', tri_releases, geometry_field='geom', fields=('year', 'f', 'frs_id', 'f_lat', 'f_long', 'industry', 'pollutant', 'cas_id', 'release', 'unit', 'clean_air', 'metal', 'carcinogen', 'medium',))
        new_tri_json = json.loads(serializer)
        # i = 0
        # for eachobj in new_tri_json['features']:
        #     facility_id = eachobj['properties']['f']
        #     try:
        #         new_tri_json['features'][i]['properties']['popupContent'] = {
        #             "Year": new_tri_json['features'][i]['properties']['year'],
        #             "Facility Id": new_tri_json['features'][i]['properties']['f'],
        #             "Industry": new_tri_json['features'][i]['properties']['industry'],
        #             "Pollutant": new_tri_json['features'][i]['properties']['pollutant'],
        #             "CAS ID": new_tri_json['features'][i]['properties']['cas_id'],
        #             "Release": new_tri_json['features'][i]['properties']['release'],
        #             "Unit": new_tri_json['features'][i]['properties']['unit'],
        #             "Clean Air Act Chemical": new_tri_json['features'][i]['properties']['clean_air'],
        #             "Metal": new_tri_json['features'][i]['properties']['metal'],
        #             "Carcinogen": new_tri_json['features'][i]['properties']['carcinogen'],
        #             "Medium": new_tri_json['features'][i]['properties']['medium'],
        #             }
        #         #new_tri_json['features'][i]['properties']['tri_facility'] = TriFacility.objects.filter(f_id = '%s').industry % facility_id
        #     except:
        #         new_tri_json['features'][i]['properties']['popupContent'] = "None"
        #         #new_tri_json['features'][i]['properties']['tri_facility'] = "None"
        #     i = i+1
        with open("C:\\Users\\MeganLuisa\\web_gis\\LeafletSlider\\examples\\test.json", 'w') as outfile:
             json.dump(new_tri_json, outfile, indent =4)
        return Response(new_tri_json)