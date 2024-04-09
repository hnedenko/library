from django.db import models
from django.contrib.postgres.fields import ArrayField


class Author(models.Model):
    name = models.CharField(max_length=100)
    gender = models.BooleanField()
    books_id = ArrayField(models.IntegerField())

    def __str__(self):
        return str(self.name) +\
               str(self.gender) +\
               str(self.books_id)
