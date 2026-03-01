from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username','first_name', 'last_name'] 
    
    email = models.EmailField(
        _("email"),
        unique=True,
        blank=False,
        null=False
        )
        
    class Meta:
        verbose_name = _('usuário')
        verbose_name_plural = _('usuários')
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return self.get_full_name() or self.username or self.email
