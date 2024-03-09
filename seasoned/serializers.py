from rest_framework import serializers
from .models import Seasoned

class SeasonedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seasoned
        fields = '__all__'