from django.db import models

from datetime import timedelta


class User(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def created_at(self):
        return self.created + timedelta(minutes=45, hours=5)

    def updated_at(self):
        return self.updated + timedelta(minutes=45, hours=5)


