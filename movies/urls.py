from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index" ),
    path('profiles/', profiles, name="profiles"),
    path('create/', createProfile, name="create"),
    path('movies/', movies, name="movies"),
    path('videos/<str:videoAdi>', videos, name="videos"),
    path('edit_profile/<int:profile_id>', edit_profile, name="edit_profile"),
    path('delete_profile/<int:profile_id>', delete_profile, name="delete_profile"),
]