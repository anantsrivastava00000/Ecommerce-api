from django.db import models
from django.contrib.auth.models import User

# Create your models here.


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Cateogry(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    


class Subcateogry(models.Model):
    name=models.CharField(max_length=100)
    Cateogry=models.ForeignKey(Cateogry, on_delete=models.CASCADE, related_name='subcateogry')
    def __str__(self):
        return self.name
    


class Product(models.Model):
    subcateogry = models.ForeignKey(Subcateogry, on_delete=models.CASCADE, related_name='product')
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    


class Color(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class Ram(models.Model):
    # values=models.CharField(max_length=100)  # meri soch
    # Arpit soch
    Ram_values=models.PositiveIntegerField()
    def __str__(self):
        return str(self.Ram_values)
    

class Storage(models.Model):
    # rom_values=models.CharField(max_length=100) #mine soch
    #Arpit Soch
    rom_values=models.PositiveIntegerField()
    def __str__(self):
        return str(self.rom_values)
     

class Product_variant(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_variant')
    image=models.ImageField(upload_to= 'photos/')
    color=models.ForeignKey(Color, on_delete=models.CASCADE, related_name='product_variant', blank=True, null=True)
    price=models.DecimalField(max_digits=10, decimal_places=2) #39000000.00
    ram=models.ForeignKey(Ram, on_delete=models.CASCADE, null=True, blank=True)
    storage=models.ForeignKey(Storage, on_delete=models.CASCADE, blank=True, null=True)

class items(models.Model):
    product_variant = models.ForeignKey(Product_variant, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()




# class Attribute():#RAM, ROM
#     pass
# class Attributevalue():#4GB, 8GB, 64GB, 128GB 
#     pass
# class Productvariant():
#     ram=
#     storage=
 


 
    


 
