from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    ingred = models.TextField(max_length=500, default='erro')
    mdf = models.TextField(max_length=1000, default = 'erro')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title