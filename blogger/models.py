from venv import create
from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["surname"]
        verbose_name_plural = "Authors"

    def __str__(self) -> str:
        return '%s %s' % (self.name, self.surname)


class Book(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    isbn = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        ordering = ["title"]
        verbose_name_plural = "Titles"

    def __str__(self):
        return '%s' % (self.title)
