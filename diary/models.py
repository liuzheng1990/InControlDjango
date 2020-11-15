from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return f"{self.name}"


class Diary(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.created_at} by {self.author.username}"
    
    def body_paragraphs(self):
        return self.body.split('\n')

    def summary(self):
        return self.body.split('\n')[0]

    def get_tags(self):
        return list(self.tags.all())

    def get_absolute_url(self):
        return f"/diary/{self.pk}/"