import random
import asyncio

from django.core.serializers import serialize
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.template import loader

from bookshop.models import Book, AuthorBook, PublisherBook


def getbook(id=None, title=None):
    try:
        if id is not None:
            return Book.objects.get(pk=id)
        elif title:
            return Book.objects.get(title=title)
    except Book.DoesNotExist:
        pass

    return


def getallbooks():
    allbooks = []

    for book in Book.objects.all():
        allbooks.append({
            'book': book,
            'authors': [authorbook.author for authorbook in AuthorBook.objects.filter(book=book)],
            'publishers': [publiserbook.publisher for publiserbook in PublisherBook.objects.filter(book=book)],
        })

    return allbooks


def getrandomcatalog(size=6):
    books = getallbooks()
    random.shuffle(books)

    return books[0:size]


def index(req: HttpRequest) -> HttpResponse:
    context = {
        'books': getrandomcatalog(),

    }

    return render(req, "index.html", context)


def error(code: int):
    pass


class BooksView(View):
    def get(self, req: HttpRequest, *args, **kwargs):
        book = getbook(**kwargs)

        if book:
            return render(req, "books.html", {'book': book})

        return render(req, "error.html", {'error': 404})


class FilmListView(BooksView, ListView):
    pass
