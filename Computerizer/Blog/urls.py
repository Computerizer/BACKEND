from django.urls import path
from . import views

urlpatterns = [
    path('authors', views.getAuthors, name='author-api')
]