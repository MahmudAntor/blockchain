from django.shortcuts import render
from device.models import Device

def localmanagement(request):
    devices = Device.objects.all()
    context = {
        'devices': devices,
    }
    return render(request, 'local/management.html', context)
