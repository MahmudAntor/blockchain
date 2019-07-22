from django.shortcuts import render
from .utils import DH_Endpoint
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from device.models import Device, Miner
from device.serializers import DevSerializer, MinSerializer
import requests
from django.http import JsonResponse


# def partial(request, key1):
#     self = Self()
#     device = DH_Endpoint(self.public_key, key1, self.private_key)
#     partial_key = device.generate_partial_key()
#     print(partial_key)
#     return HttpResponse('This is the partial')


@api_view(['GET', 'POST'])
def device_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        devices = Device.objects.all()
        serializer = DevSerializer(devices, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DevSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def device_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        device = Device.objects.get(pk=pk)
    except Device.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DevSerializer(device)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DevSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




def cripto_connect(request):
    p_key = 7919
    device = Device.objects.get(public_key = p_key)
    # serializer = DevSerializer(device)
    # payload = {'key1': serializer.data}
    content = requests.get('http://127.0.0.1:8002/cripto/19')
    gdata = content.json()
    context = {
        'par' : gdata['partial'],
    }
    device.partial = gdata['partial']
    device.save()
    miner = Miner()
    med = DH_Endpoint(miner.public_key, p_key, miner.private_key)
    device.dh_key = med.generate_full_key(device.partial)
    device.save()

    print(context)
    return HttpResponseRedirect(reverse('home'))



@api_view(['GET'])
def partial(request, pk):
    miner = Miner.objects.get(pk = 19)

    min = DH_Endpoint(miner.public_key, pk, miner.private_key)
    miner.partial = min.generate_partial_key()
    miner.save()
    print(miner.partial)
    serializer = MinSerializer(miner)
    return Response(serializer.data)