import imp
from .models import Postes
from rest_framework import serializers

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Postes
        fields = '__all__'

    