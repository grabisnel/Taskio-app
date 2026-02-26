from django.db import models
from django.conf import settings

# Create your models here.

class Task(models.Model):

    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        IN_PROGRESS = 'in_progress', 'In Progress'
        COMPLETED = 'completed', 'Completed'

    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=150, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    class Meta:
        db_table = 'task'

    def __str__(self):
        return self.title
        
    
    
    