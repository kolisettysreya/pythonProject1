from django.db import models

class IceCream(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Example price field


    def __str__(self):
        return self.name


'''
from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through='CartItem')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
'''
from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    comments = models.TextField(max_length=150)

    def str(self):
        return self.name
from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name= models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images/')
    price = models.CharField(max_length=7)
    category = models.ManyToManyField('Category', related_name="item")
    def _str_(self):
        return self.name

class category(models.Model):
    name = models.CharField(max_length=100)
    def _str_(self):
        return self.name

class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=7)
    items = models.ManyToManyField('MenuItem',related_name='order', blank= True)
    name = models.CharField(max_length=50, blank= True)
    email = models.CharField(max_length=50, blank= True)
    phone = models.CharField(max_length=20, blank=True)
    is_shipped=models.BooleanField(default=False)

    def _str_(self):
        return f'Order:{self.created_on.strftime("%b %d %I: %M %p")}'







