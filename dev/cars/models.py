from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    menu_category_item = models.CharField(max_length=200)
    
class Menu(models.Model):
    menu_item = models.CharField(max_length=200)
    price = models.IntegerField()
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None)
    