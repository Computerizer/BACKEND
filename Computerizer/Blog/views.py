from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Author
from .serializer import AuthorSerializer

# Create your views here.

@api_view(["GET"])
def getAuthors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)