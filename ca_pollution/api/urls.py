from . import views
from .views import TriReleaseList
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('tri_releases/', views.TriReleaseList.as_view(), name='tri_releases'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
