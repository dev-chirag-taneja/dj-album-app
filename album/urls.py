from django.urls import path

from .views import *

urlpatterns = [
    path("", gallery, name="gallery"),
    path("photo/<str:pk>/", photo, name="photo"),
    path("add/", add, name="add"),
]
