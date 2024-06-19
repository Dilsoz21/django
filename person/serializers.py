from rest_framework import serializers
from .models import Person

class PoetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("name", "content")

