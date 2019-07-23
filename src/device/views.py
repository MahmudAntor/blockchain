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
from local.models import *
from django.contrib import messages


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
    miner =  Miner.objects.get(public_key = 19)
    med = DH_Endpoint(miner.public_key, p_key, miner.private_key)


    # add genesis block
    block = Block.objects.latest('id')
    print(block)
    try:
        policy = PolicyHeader.objects.get(
            requester = request.user,
            requested_action = PolicyHeader.GENESIS,
            device = device,
            action = PolicyHeader.ALLOW,
        )
        true = policy in block.policy_header.all()

    except:

        messages.warning(request, 'You don\'t have Permission to add this transaction')
        return HttpResponseRedirect(reverse('local:local'))

    else:

        device.dh_key = med.generate_full_key(device.partial)
        device.save()
        transaction = Transactions(
            transaction_number = 1,
            device = device,
            transaction_type = Transactions.GENESIS,
        )
        transaction.save()
        block.transactions.add(transaction)

        return HttpResponseRedirect(reverse('local:local'))


@api_view(['GET'])
def partial(request, pk):
    miner = Miner.objects.get(public_key = 19)
    min = DH_Endpoint(miner.public_key, pk, miner.private_key)
    miner.partial = min.generate_partial_key()
    miner.save()
    print(miner.partial)
    serializer = MinSerializer(miner)
    return Response(serializer.data)