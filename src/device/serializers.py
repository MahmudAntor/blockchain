from rest_framework import serializers
from .models import Device, Miner
from local.models import BlockHeader


class DevSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id','public_key']

class MinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miner
        fields = ['partial']

class GlobSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockHeader
        fields = ['hash']
