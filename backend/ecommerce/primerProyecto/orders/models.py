from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
   
class Country(models.Model):
    name = models.CharField(max_length=100)
    status_id = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.name}'

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.name}'

class Municipality(models.Model):
    municipality_id = models.AutoField(primary_key=True)
    departament = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


    
class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    telephoneNumber = models.CharField(max_length=50, default='')
    id_status = models.BooleanField(default=True)
    dateCreated = models.DateTimeField(default=timezone.now)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=1)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    city = models.ForeignKey(Municipality, on_delete=models.CASCADE, default=1)
    address = models.CharField(max_length=50, default='Escriba su direccion')
    def __str__(self):
        return f'User ({self.id}): {self.user.username} {self.telephoneNumber}'
    
class ProductCategory(models.Model):
    category_id =models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    categoryImage = models.ImageField(upload_to='products/', blank=True, null=True)
    description =models.TextField(max_length=500, null=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    productCategory_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    sellPrice = models.FloatField(null=True)
    description =models.TextField(max_length=500, null=True)
    productImage = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Car(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CarItem')

    def __str__(self):
        return f"Carro de  {self.cliente.username}"
    
class CarItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    cantidad = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.cantidad}x {self.product.name}"

# class SalesCheck(models.Model):
#     salesCheck_id = models.AutoField(primary_key=True)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     cantidad = models.IntegerField(default=1)
#     dateBill = models.DateField()
#     fullValue = models.IntegerField(default=1)

    
#contraseña 1Q2w3e4rE


    

    

    