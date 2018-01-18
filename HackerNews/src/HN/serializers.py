from rest_framework import serializers
from HN.models import Hnews

class HnewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hnews
        fields = ('title','id')
