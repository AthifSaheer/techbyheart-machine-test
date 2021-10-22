from django.db import models
from django.contrib.auth.models import User
from superadmin.models import *

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "User: " + str(self.user) + " | Store: " + str(self.store)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "User: " + str(self.user) + " | Product: " + str(self.product)
