from django.db import models


# Description
class UserDescription(models.Model):
    description = models.TextField()
    tools = models.TextField()

    def __str__(self):
        return "{self.description}, {self.tools}"


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website_link = models.URLField()
    photos = models.ImageField(upload_to='uploads/project_photos/')

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/portfolio_photos/')

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"