from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from device import views

urlpatterns = [
    path('', views.device_list),
    path('partial/<int:pk>', views.partial),
    path('<int:pk>', views.device_detail),
    path('try/', views.cripto_connect),
]

urlpatterns = format_suffix_patterns(urlpatterns)