from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView, FollowBookView

urlpatterns = [
    path("books/", BookListCreateView.as_view()),
    path("books/<int:pk>/", BookRetrieveUpdateDestroyView.as_view()),
    path("follow/<int:pk>/", FollowBookView.as_view(), name="follow-book"),
]
