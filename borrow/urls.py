from django.urls import path
from .views import BorrowingBookView, BorrowingBookDetailView

urlpatterns = [
    path("borrowing_book/", BorrowingBookView.as_view()),
    path("borrowing_book/<int:pk>/", BorrowingBookDetailView.as_view()),
]