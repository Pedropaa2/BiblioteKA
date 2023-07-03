from rest_framework import serializers
from .models import Copy

class CopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = ['id', 'book', 'condition', 'paperback', 'quantity', 'reviews']

    def create(self, validated_data):
        return Copy.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.condition = validated_data.get('condition', instance.condition)
        instance.paperback = validated_data.get('paperback', instance.paperback)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.reviews = validated_data.get('reviews', instance.reviews)
        instance.save()
        return instance