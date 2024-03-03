from django.db import models

class Creators(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Product(models.Model):
    creator_id = models.ForeignKey(Creators, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=30)
    date = models.DateTimeField()
    price = models.IntegerField()
    def __str__(self):
        return f'Продукт: {self.product_name}'

class ProductMaxMinMembers(models.Model):
    product_id = models.OneToOneField(Product,on_delete=models.CASCADE,related_name="Min_Max_of",)
    maxMembers = models.IntegerField()
    minMembers = models.IntegerField()
    def __str__(self):
        return self.product_id.product_name

class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=320,unique=True)
    def __str__(self):
        return self.email

class UsersProducts(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    access = models.BooleanField()
    def __str__(self):
        return self.user_id + ' ' + self.product_id + ' ' + self.access
    
class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length=30,unique=True)
    description = models.CharField(max_length=255)
    url = models.TextField()
    def __str__(self):
        return self.lesson_name

class Group(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=30)
    members = models.ManyToManyField(Users)
    def __str__(self):
        return self.group_name
