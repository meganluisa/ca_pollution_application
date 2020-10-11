from django.urls import path
from django.contrib import admin
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static
#from django.views.generic import TemplateView

urlpatterns = [
    #path('tri_releases/', views.TriReleaseList.as_view(), name='tri_releases'),
    path('', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)