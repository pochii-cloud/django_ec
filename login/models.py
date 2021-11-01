from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Contact(models.Model):
    username=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=20,default='')
    message=models.TextField(max_length=500)

    def __str__(self):
        return self.username

class Product(models.Model):
    Category=models.ForeignKey(Category,on_delete=models.CASCADE,null=False,blank=False,default=0)
    name=models.CharField(max_length=100,default='')
    description=models.CharField(max_length=300,default='')
    image=models.ImageField(upload_to="img")
    price=models.IntegerField(max_length=100,default=0)
    date_added=models.DateTimeField(auto_now='True')

    class Meta:
        ordering=['-date_added']

    def __str__(self):
        return  self.name

class Enquire(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True,default='')
    name=models.CharField(max_length=50)
    number=models.CharField(max_length=15)

    def __str__(self):
        return self.product.name

class Post(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(default='')
    body=models.TextField(max_length=2000)
    date_added=models.DateTimeField(auto_now='True')
    slug=models.SlugField(max_length=1000,default='')

    class Meta:
     ordering=['-date_added']

    def __str__(self):
        return self.title