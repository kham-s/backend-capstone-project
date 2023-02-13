from django.db import models

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200, default='')
    no_of_guests = models.IntegerField(default=1)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self):
        return self.first_name

# Add code to create Menu model
class Menu(models.Model):
   title = models.CharField(max_length=200) 
   price = models.DecimalField(max_digits=10, decimal_places=2) 
   inventory = models.IntegerField(default=0) 
   menu_item_description = models.TextField(max_length=1000, default='') 

   def __str__(self):
        return self.title