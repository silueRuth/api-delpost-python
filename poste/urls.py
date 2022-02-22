from . import views
from django.urls import path

urlpatterns = [
    path('deletepost/<int:id>', views.delete_post),
]