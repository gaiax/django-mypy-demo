from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.db.models.query import QuerySet

from .models import Book
from typing import Dict

ContextType = Dict[str, "QuerySet[Book]"]


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "books/index.html")


def show_books(request: HttpRequest) -> HttpResponse:
    books: "QuerySet[Book]" = Book.objects.all()
    context: ContextType = {"books": books}
    return render(request, "books/show.html", context)
