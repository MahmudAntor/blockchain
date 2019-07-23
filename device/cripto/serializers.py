from rest_framework import serializers
from .models import Self, GlobalChain


class SelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Self
        fields = ['id','public_key', 'private_key', 'df_key', 'partial']

class PartialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Self
        fields = ['partial']


class GlobalSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalChain
        fields = ['hash']
