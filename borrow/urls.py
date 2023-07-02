from django.urls import path
from .views import BorrowingBookView, BorrowingBookDetailView

urlpatterns = [
    path("borrowing-book/", BorrowingBookView.as_view()),
    path("borrowing-book/<int:pk>/", BorrowingBookDetailView.as_view()),
]