from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class User(models.Model):
    firstname = models.CharField(max_length=24, null=False)
    lastname = models.CharField(max_length=24, null=False)
    nickname = models.CharField(max_length=18, null=False)
    email = models.EmailField(null=True)

    def __str__(self):
        return f"{self.nickname}"


class Author(models.Model):
    firstname = models.CharField(max_length=24)
    lastname = models.CharField(max_length=24)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Publisher(models.Model):
    name = models.CharField(max_length=86, null=False, blank=False)
    address = models.TextField(blank=True)
    website = models.TextField(blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=24, null=False)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=86, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    edition = models.IntegerField(null=True)
    description = models.TextField(null=False)
    quantity = models.PositiveIntegerField(null=False)
    price = models.PositiveIntegerField(null=False)

    def __str__(self):
        return f"{self.title}"


class AuthorBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title} ({self.book.date.year}), {str(self.author)}"


class PublisherBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title} ({self.book.date.year}), {str(self.publisher)}"
