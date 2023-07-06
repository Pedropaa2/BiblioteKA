from django.urls import path
from . import views

urlpatterns = [
    path("copy/create/<int:pk>/", views.CopyView.as_view()),
    path("copy/<int:pk>/", views.CopyDetailView.as_view()),
    path("copy/", views.AllCopyView.as_view()),
]
