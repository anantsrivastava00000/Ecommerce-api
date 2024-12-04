from django.contrib import admin
from .models import*
# Register your models here.

@admin.register(Cateogry)
class CateogryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Subcateogry)
class SubcateogryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'Cateogry']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subcateogry']    


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Ram)
class RamAdmin(admin.ModelAdmin):
    list_display = ['id', 'Ram_values']

@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ['id', 'rom_values']

@admin.register(Product_variant)
class Product_variantAdminAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'image', 'color', 'price', 'ram', 'storage']

