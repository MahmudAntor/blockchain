from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from device import views
from django.urls import path
from django.conf.urls import url

app_name = "device"
urlpatterns = [
    path('partial/<int:pk>', views.partial),
    path('', views.cripto_connect, name="connect"),
    path('<int:id>/alter', views.alter, name='alter'),
    path('global/<int:hash>', views.return_global),
]

urlpatterns = format_suffix_patterns(urlpatterns)