from rest_framework import serializers
from .models import Fresher

class FresherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fresher
        fields = '__all__'
