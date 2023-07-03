from django.urls import path
from .views import BorrowingBookView, BorrowingBookDetailView

urlpatterns = [
    path("borrow/", BorrowingBookView.as_view()),
    path("borrow/<int:pk>/", BorrowingBookDetailView.as_view()),
]
