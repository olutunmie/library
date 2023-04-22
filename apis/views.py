from rest_framework import generics
from django.shortcuts import render

from books.models import Book
from apis.serializer import BookSerializer


# Create your views here.
class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
