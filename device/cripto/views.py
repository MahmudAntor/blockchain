from .utils import DH_Endpoint
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cripto.models import Self, Miner
from cripto.serializers import SelfSerializer, PartialSerializer
import requests



@api_view(['GET'])
def cripto_detail(request, pk):

    cripto = Self.objects.get(public_key=7919)

    device = DH_Endpoint(cripto.public_key, pk, cripto.private_key)
    cripto.partial = device.generate_partial_key()
    cripto.save()
    print(cripto.partial)
    #return HttpResponse('This is the partial')
    serializer = PartialSerializer(cripto)



    miner_per = requests.get('http://127.0.0.1:8000/device/partial/7919')
    par = miner_per.json()
    print(par)
    device = Self.objects.get(public_key=7919)
    device.partial = par['partial']
    device.save()
    med = DH_Endpoint(device.public_key, 19, device.private_key)
    device.dh_key = med.generate_full_key(device.partial)
    device.save()

    return Response(serializer.data)



