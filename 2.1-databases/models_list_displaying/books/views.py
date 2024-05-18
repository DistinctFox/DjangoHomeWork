from django.shortcuts import render
from django.http import HttpResponse
from models_list_displaying.books.models import Phone


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)
