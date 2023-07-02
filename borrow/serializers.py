from rest_framework import serializers
from .models import Borrow


class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = '__all__'

    def create(self, validated_data):
        borrow = Borrow.objects.create(**validated_data)
        return borrow

    def update(self, instance, validated_data):
        instance.return_date = validated_data.get(
            'return_date',
            instance.return_date
            )
        instance.save()
        return instance
