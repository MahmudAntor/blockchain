from django.shortcuts import render
from device.models import Device
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect



def localmanagement(request):
    if request.user.is_authenticated:

        devices = Device.objects.all()
        context = {
            'devices': devices,
        }
        return render(request, 'local/management.html', context)
    else:
        return HttpResponseRedirect(reverse('home'))