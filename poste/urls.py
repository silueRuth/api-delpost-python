from . import views
from django.urls import path

urlpatterns = [
    path('deletepost/', views.delete_post),
]