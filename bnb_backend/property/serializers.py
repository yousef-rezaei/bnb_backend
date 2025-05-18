from rest_framework import serializers

from .models import Property


class PropertiesListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            'id',
            'title',
            'price_per_night',
            "image_url",
        ]