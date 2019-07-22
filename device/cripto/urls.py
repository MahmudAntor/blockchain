from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from cripto import views

urlpatterns = [
    # path('cripto/', views.cripto_list),
    path('cripto/<int:pk>', views.cripto_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)