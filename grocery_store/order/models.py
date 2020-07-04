from django.db import models
from django.contrib.auth.models import User
class Order(models.Model):
    token=models.CharField(max_length=250,blank=True)
    username=models.CharField(max_length=100,blank=True)
    total=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='G&P Order Total')
    emailAddress=models.EmailField(max_length=250,blank=True,verbose_name='Email Address')
    created=models.DateTimeField(auto_now_add=True)
    billingName=models.CharField(max_length=250,blank=True)
    billingAddress1=models.CharField(max_length=250,blank=True)
    billingCity=models.CharField(max_length=250,blank=True)
    billingPostcode=models.CharField(max_length=10,blank=True)
    billingCountry=models.CharField(max_length=250,blank=True)
    shippingName=models.CharField(max_length=250,blank=True)
    shippingAddress1=models.CharField(max_length=250,blank=True)
    shippingCity=models.CharField(max_length=250,blank=True)
    shippingPostcode=models.CharField(max_length=10,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    shippingCountry=models.CharField(max_length=250,blank=True)

    class Meta:
        db_table='Order'
        ordering=['-created']

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product=models.CharField(max_length=250)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Price')
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        db_table='OrderItem'
    def sub_total(self):
        return self.quantity*self.price
    def __str__(self):
        return self.product
