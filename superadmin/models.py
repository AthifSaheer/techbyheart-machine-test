from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.PositiveIntegerField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class StoreProduct(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Store: " + str(self.store) + " - product: " + str(self.product)

