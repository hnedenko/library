from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, blank=False)
    gender = models.BooleanField(blank=True)
    books = models.ManyToManyField('Book', blank=True, related_name='authors')

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    title = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return str(self.title)
