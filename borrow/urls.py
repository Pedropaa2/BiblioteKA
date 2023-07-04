from django.urls import path
from .views import BorrowBooksView, BorrowingBookView, BorrowingBookDetailView

urlpatterns = [
    path("borrow/", BorrowBooksView.as_view()),
    path("borrow/<str:username>/<int:pk>/", BorrowingBookView.as_view()),
    path("borrow/<int:pk>/", BorrowingBookDetailView.as_view()),
]
