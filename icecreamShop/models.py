from django.db import models
from django.core.validators import MinValueValidator
from accounts.models import Customer
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='product/images')
    price = models.IntegerField(validators=[MinValueValidator(20)])
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    catetgory = models.ForeignKey(Category,on_delete=models.CASCADE) # models.CASCADE means that when the cateogry is deleted from the category model the all the products from the category will also get deleted
    description = models.TextField(max_length=100,null=True,default='')
    availble = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

class CartItem(models.Model):
    item= models.ForeignKey(Product,on_delete=models.CASCADE)
    user= models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)