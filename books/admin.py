from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "publisher"]


admin.site.register(Book, BookAdmin)
