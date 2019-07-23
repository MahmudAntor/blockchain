from django.urls import path
from . import views
from django.urls import path
from django.conf.urls import url

app_name = "local"
urlpatterns = [
    path("", views.localmanagement, name="local"),
]
