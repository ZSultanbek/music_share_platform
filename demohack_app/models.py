from django.db import models

class Post(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class Author(models.Model):
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.username