from django.contrib import admin
from .models import Category, Product, Review, Rate

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'created_at']
    list_filter = ['created_at']
    search_fields = ['text', 'user__username']

admin.site.register(Rate)

