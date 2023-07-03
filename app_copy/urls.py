from django.urls import path
from . import views

urlpatterns = [
    path("copy/<int:pk>/", views.CopyView.as_view()),
    path("copy/<int:pk>/", views.CopyDetailView.as_view()),
]
