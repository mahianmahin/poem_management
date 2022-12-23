from django.db import models


class Poems(models.Model):
    poem = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    added_to_book = models.BooleanField(default=False)
