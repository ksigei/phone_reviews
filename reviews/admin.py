from django.contrib import admin
from .models import Category, Product, Review, Rate

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Rate)
