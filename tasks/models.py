from django.db import models
import uuid

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True, null=True)
    completed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['title', 'completed', 'description']

    def __str__(self):
        return self.title