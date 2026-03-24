from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    credit = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name

class Transaction(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        rstring = self.student.name + " a commandé un " + self.product.name
        return rstring
