from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class restaurant(models.Model):
    rs = (
        (1, "Close"),
        (2, "Open"),
    ) 
    restaurant_name = models.CharField(max_length=50)
    seller_phone = models.CharField(max_length=10)
    desc = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='restaurant_image', blank=True)
    restaurant_status = models.IntegerField(choices=rs)

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

class order_list(models.Model):
    desc = models.CharField(max_length=200)
    unit = models.CharField(max_length=10)
    unit_price = models.FloatField()
    order_order_id = models.ForeignKey(User, on_delete=models.CASCADE)

class order(models.Model):
    pm = (
        (1, "No"),
        (2, "Yes"),
    )
    os = (
        (1, "No"),
        (2, "Yes"),       
    )
    order_date = models.DateTimeField(auto_now_add=True)
    payment  = models.IntegerField(choices=pm)
    list_price = models.FloatField()
    order_status = models.IntegerField(choices=os)
    customer_user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class customer(models.Model):
    rs = (
        (1, "reserve"),
        (2, "no"),
    )
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    cus_phone = models.CharField(max_length=10)
    resecus_status = models.IntegerField(choices=rs)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class admin(models.Model):
    contact = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class comment(models.Model):
    comment_detail = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(restaurant, on_delete=models.CASCADE)

class admin_customer(models.Model):
    customer_user_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    admin_user_id = models.ForeignKey(admin, on_delete=models.CASCADE)

class menu_order_list(models.Model):
    menu_menu_id = models.ForeignKey(restaurant_menu, on_delete=models.CASCADE)
    order_list_list_id = models.ForeignKey(order_list, on_delete=models.CASCADE)