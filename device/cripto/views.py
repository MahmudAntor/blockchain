from .utils import DH_Endpoint
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cripto.models import Self
from cripto.serializers import SelfSerializer, PartialSerializer
import requests


@api_view(['GET', 'POST'])
def partial(request):
    self = Self()
    key1=5
    device = DH_Endpoint(self.public_key, key1, self.private_key)
    partial_key = device.generate_partial_key()
    print(partial_key)
    return HttpResponse('This is the partial')



def td(request):
    return HttpResponseRedirect('http://127.0.0.1:8000/users/me/')



# @api_view(['GET', 'POST'])
# def cripto_list(request, format=None):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         criptos = Self.objects.all()
#         serializer = SelfSerializer(criptos, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = SelfSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def cripto_detail(request, pk):

    cripto = Self.objects.get(public_key=7919)

    device = DH_Endpoint(cripto.public_key, pk, cripto.private_key)
    cripto.partial = device.generate_partial_key()
    cripto.save()
    print(cripto.partial)
    #return HttpResponse('This is the partial')
    serializer = PartialSerializer(cripto)


    # partial = requests.get('http://127.0.0.1:8000/device/partial/7919')
    # par = partial.json()
    # print(par)


    return Response(serializer.data)
