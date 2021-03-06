from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='article')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, related_name='article')

    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='article/', null=False, blank=False)
    content = models.TextField(null=True, blank=True)

    created_at = models.DateField(auto_created=True, null=True)

