from django.db import models
from django.contrib.auth.models import User
from superadmin.models import *

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "User: %s | Product: %s", self.user, self.product