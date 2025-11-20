from django.db import models

# Create your models here.


class Task(models.Model):
    
    name = models.CharField(max_length=150, blank=False, null=False)
    completed = models.BooleanField(default=False)
    description = models.CharField(max_length=150, null=True)
    created_date = models.DateTimeField(auto_now=True)
    completed_date = models.DateTimeField(null=True)
    
    class Meta: 
        db_table = 'task'
        
    def _str_(self):
        return self.name
        
    
    
    