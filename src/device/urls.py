from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from device import views

urlpatterns = [
    path('partial/<int:pk>', views.partial),
    path('', views.cripto_connect),
]

urlpatterns = format_suffix_patterns(urlpatterns)