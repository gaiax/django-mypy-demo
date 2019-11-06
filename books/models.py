from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
