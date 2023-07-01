from rest_framework import generics
from .models import Borrow
from .serializers import BorrowSerializer


class BorrowingBookView(generics.ListCreateAPIView):
    queryset = Borrow.objects.filter(is_returned=False)
    serializer_class = BorrowSerializer


class BorrowingBookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

    def perform_destroy(self, instance):
        if instance.is_retuned:

            instance.copy.quantity += 1
            instance.copy.save()

            instance.copy.is_retuned = True
            instance.copy.save()

            instance.is_retuned = True
            instance.save()
