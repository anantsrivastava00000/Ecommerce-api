from django.contrib import admin
from .models import Other, Othervalue, Product_Variant
# Register your models here.
@admin.register(Other)
class OtherAdmin(admin.ModelAdmin):
    list_display=['id', 'name']

@admin.register(Othervalue)
class OtherAdmin(admin.ModelAdmin):
    list_display=['id', 'values', 'other']

 
@admin.register(Product_Variant)
class Product_VariantAdmin(admin.ModelAdmin):
    list_display=['id','Ram']


