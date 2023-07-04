from rest_framework import serializers
from .models import Borrow
from datetime import timedelta
from django.utils import timezone


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
            # "user",
            # "copy",
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

        if return_date < timezone.now():
            borrow.is_delay = True
            borrow.is_active = False
            borrow.blocking_end_date = timezone.now() + timedelta(days=7)

        if borrow.is_returned:
            borrow.is_active = False
            borrow.blocking_end_date = timezone.now() + timedelta(days=7)

        borrow.return_date = return_date
        borrow.save()

        borrow.copy.quantity -= 1
        borrow.copy.save()
        return borrow

    def update(self, instance, validated_data):
        instance.return_date = validated_data.get(
            'return_date',
            instance.return_date
            )
        instance.save()
        return instance

    # def perform_create(self, serializer):
        #  if not serializer.validated_data.get('return_date'):
        #      borrow_date = serializer.validated_data['borrow_date']
        #      return_date = borrow_date + timedelta(days=3)
        #      if return_date.weekday() in [5, 6]:
        #          return_date += timedelta(days=3 - return_date.weekday())

        #      if return_date < timezone.now():
        #          serializer.validated_data['is_delay'] = True
        #          serializer.validated_data['is_active'] = False
        #          serializer.validated_data[
        #              'blocking_end_date'
        #              ] = timezone.now() + timedelta(days=7)

        #      if serializer.validated_data['is_returned']:
        #          serializer.validated_data['is_active'] = False
        #          serializer.validated_data[
        #              'blocking_end_date'
        #              ] = timezone.now() + timedelta(days=7)

        #      serializer.validated_data['return_date'] = return_date

    #     instance = serializer.save()

    #     instance.user.update_blocked_status()
