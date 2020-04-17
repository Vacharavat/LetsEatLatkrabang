from django.db import models

# Create your models here.
class restaurant(models.Model):
    restaurant_name = models.CharField(max_length=50)
    seller_phone = models.CharField(max_length=10)
    desc = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='restaurant_image', blank=True)
    restaurant_status = models.DateField()

class restaurant_type(models.Model):
    type_name = models.CharField(max_length=50)
    restaurant_id = models.ForeignKey(restaurant, on_delete=models.CASCADE)

class location(models.Model):
    location_address = models.CharField(max_length=200)
    restaurant_id = models.ForeignKey(restaurant, on_delete=models.CASCADE)

class restaurant_menu(models.Model):
    menu_name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='menu_image', blank=True)
    menu_price = models.FloatField()
    restaurant_id = models.ForeignKey(restaurant, on_delete=models.CASCADE)