from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class Customer(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=25)
    ContactName = models.CharField(max_length=25)
    Address = models.CharField(max_length=25)
    City = models.CharField(max_length=10)
    PostalCode = models.IntegerField()
    Country = models.CharField(max_length=20)
   
    
def __str__(self):
    return self.name



class Category(models.Model):
    CategoryID = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=25)
    Description = models.TextField(blank=True)
    
    
def __str__(self):
    return self.name

class Employee(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    LastName = models.CharField(max_length=25)
    FirstName = models.CharField(max_length=25)
    BirthDate = models.DateField()
    Photo = models.ImageField(upload_to="images", blank=True, null=True)   
    Notes  = models.TextField(blank=True)
    
def __str__(self):
    return self.name

class OrderDetail(models.Model):
    OrderDetailID = models.AutoField(primary_key=True)
    OrderID = models.IntegerField()
    ProductID = models.IntegerField()
    Quantity = models.IntegerField()
    
    
def __str__(self):
    return self.name

class Order(models.Model):
    OrderID = models.AutoField(primary_key=True)
    CustomerID = models.IntegerField()
    EmployeeID = models.IntegerField()
    OrderDate = models.DateField()
    ShipperID = models.IntegerField()  
    
def __str__(self):
    return self.name


class Product(models.Model):
    ProductID = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=25)
    SupplierID = models.IntegerField()
    CategoryID = models.IntegerField()   
    Unit  = models.CharField(max_length=25)
    Price = models.IntegerField()
    image = models.ImageField(upload_to="images", blank=True, null=True)
    description = models.TextField()
    
def __str__(self):
    return self.name

class Shipper(models.Model):
    ShipperID = models.AutoField(primary_key=True)
    ShipperName = models.CharField(max_length=25)
    Phone = models.CharField(max_length=25)
    
    
def __str__(self):
    return self.name

class Supplier(models.Model):
    SupplierID = models.AutoField(primary_key=True)
    SupplierName = models.CharField(max_length=25)
    ContactName = models.CharField(max_length=25)
    Address = models.CharField(max_length=25)
    City = models.CharField(max_length=10)
    PostalCode = models.IntegerField()
    Country = models.CharField(max_length=20)
    Phone = models.CharField(max_length=25)
    
def __str__(self):
    return self.name

class Contact(models.Model):
    ProductID = models.AutoField(primary_key=True)
    Nama = models.CharField(max_length=25)
    Email = models.EmailField()
    Message = models.TextField()

   
    
def __str__(self):
    return self.name