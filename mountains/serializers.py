from rest_framework.serializers import ModelSerializer

from mountains.models import Mountain


class MountainsSerializer(ModelSerializer):
    class Meta:
        model = Mountain
        fields = [
            'pk',
            'name',
            'altitude',
            'lat',
            'long',
            'location',
            'created_at',
            'updated_at'
        ]
        read_only_fields = [
            'pk',
            'location',
            'created_at',
            'updated_at',
        ]
