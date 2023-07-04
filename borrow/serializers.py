from rest_framework import serializers
from .models import Borrow
from datetime import timedelta
from django.utils import datetime_safe


class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = [
            "id",
            "borrow_date",
            "return_date",
            "is_delay",
            "is_active",
            "is_returned",
            "blocking_end_date",
        ]
        read_only_fields = [
              "id",
              "borrow_date",
              "return_date",
              "is_delay",
              "is_active",
              "is_returned",
              "blocking_end_date"
              "user",
              "copy",
         ]

    def create(self, validated_data):
        borrow = Borrow.objects.create(**validated_data)
        borrow_date = borrow.borrow_date
        return_date = borrow_date + timedelta(days=3)

        if return_date.weekday() in [5, 6]:
            return_date += timedelta(days=3 - return_date.weekday())

        if return_date < datetime_safe.datetime.now():
            borrow.is_delay = True
            borrow.is_active = False
            borrow.blocking_end_date = datetime_safe.datetime.now() + timedelta(days=7)

        if borrow.is_returned:
            borrow.is_active = False
            borrow.blocking_end_date = datetime_safe.datetime.now() + timedelta(days=7)

        borrow.return_date = return_date
        borrow.save()

        borrow.copy.quantity -= 1
        borrow.copy.save()
        return borrow


class BorrowDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = [
            "id",
            "borrow_date",
            "return_date",
            "is_delay",
            "is_active",
            "is_returned",
            "blocking_end_date",
        ]
        read_only_fields = [
              "id",
              "borrow_date",
              "is_delay",
              "is_active",
              "is_returned",
              "blocking_end_date"
              "user",
              "copy",
         ]

    def update(self, instance, validated_data):
        return_date = validated_data.get('return_date')

        instance.return_date = return_date
        instance.save()
        return instance

    #     instance.user.update_blocked_status()
