from django.contrib.gis.db import models
from rest_framework.response import Response
from ca_pollution.models import TriRelease, TriFacility, DmrRelease, DmrFacility
from rest_framework.views import APIView
from django.core.serializers import serialize
import json
from rest_framework import generics, viewsets
from rest_framework import generics
from django.contrib.gis.serializers.geojson import Serializer 



class CustomSerializer(Serializer):
    def end_object(self, obj):
        for field in self.selected_fields:
            if field == 'pk':
                continue
            elif field in self._current.keys():
                continue
            else:
                try:
                    if '__' in field:
                        fields = field.split('__')
                        value = obj
                        for f in fields:
                            value = getattr(value, f)
                        if value != obj:
                            self._current[field] = value

                except AttributeError:
                    pass
        super(CustomSerializer, self).end_object(obj)

class TriReleaseList(APIView):
    def get(self, request):
        serializers = CustomSerializer()
        tri_releases = TriRelease.objects.select_related('f').all()[:50]
        data = serializers.serialize(tri_releases, geometry_field='geom', fields=('year', 'frs_id', 'f_lat', 'f_long', 'industry', 'pollutant', 'cas_id', 'release', 'unit', 'clean_air', 'metal', 'carcinogen', 'medium', 'f__f_name', 'f__f_id', 'f__address', 'f__city', 'f__county', 'f__st', 'f__zip', 'f__federal'))
        new_tri_json = json.loads(data)   
                #only_features = new_tri_json.get('features')
        # with open("C:\\Users\\MeganLuisa\\web_gis\\thesis_project\\templates\\all.json", 'w') as outfile:
        #     json.dump(new_tri_json, outfile, indent =4)
         
        return Response(new_tri_json)


class DmrReleaseList(APIView):
  def get(self, request):
    serializers = CustomSerializer()
    dmr_releases = DmrRelease.objects.filter(year__year=2020)[:50]
    data = serializers.serialize(dmr_releases, geometry_field='geom', fields=('year', 'permit_num__f_name', 'geom', 'watershed', 'pollutant', 'cas_id', 'total_lbs', 'twpe', 'dfr_link'))
    new_dmr_json = json.loads(data)
    # only_features = new_dmr_json.get('features')
    # with open("C:\\Users\\MeganLuisa\\web_gis\\thesis_project\\ca_pollution\\static\\dmr_data.json", 'a') as outfile:
    #   json.dump(only_features, outfile, indent =4)
    return Response(new_dmr_json)