from django.db import models
from django.contrib.postgres.fields import ArrayField


class Book(models.Model):
    title = models.CharField(max_length=100)
    tags = ArrayField(models.CharField(max_length=50))
    authors_id = ArrayField(models.IntegerField())

    def __str__(self):
        return str(self.title) +\
               str(self.tags) +\
               str(self.authors_id)
