from django.contrib import admin

import bookshop.models

models = [
    bookshop.models.Book,
    bookshop.models.Author,
    bookshop.models.User,
    bookshop.models.Publisher,
    bookshop.models.Category,
    bookshop.models.AuthorBook,
    bookshop.models.PublisherBook,
]

for model in models:
    admin.site.register(model)
