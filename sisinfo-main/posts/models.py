from django.db import models
from django.conf import settings


class Receita(models.Model):
    title = models.CharField(max_length=200)
    ingred = models.TextField(max_length=500, default='erro')
    mdf = models.TextField(max_length=1000, default = 'erro')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.title}'