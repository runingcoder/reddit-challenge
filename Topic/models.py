from django.db import models

# Create your models here.
class Topic(models.Model):

    name = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    Urlname = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text