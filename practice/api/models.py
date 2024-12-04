from django.db import models

# Create your models here.
class Other(models.Model):
    name=models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Othervalue(models.Model):
    other=models.ForeignKey(Other, on_delete=models.CASCADE)
    values=models.PositiveIntegerField()
    def __str__(self):
        return str(self.other)

class Product_Variant(models.Model):
    Ram=models.ForeignKey(Othervalue, on_delete=models.CASCADE)
     
    