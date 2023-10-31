from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True) 
    asset = models.CharField(max_length=100)
    ITEM_TYPES = (
        ('Generator', 'Generator'),
        ('Panels', 'Panels'),
        ('ACs', 'ACs'),
        ('Inverters', 'Inverters'),
        ('Cables', 'Cables'),
        ('Lights', 'Lights'),
        ('Batteries', 'Batteries'),
        ('Others', 'Others'),
    )
    item_type = models.CharField(max_length=20, choices=ITEM_TYPES)
    unit_price = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.asset
