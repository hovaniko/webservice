# api/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DocView

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^clients/$', DocView.as_view(), name="DocView"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
