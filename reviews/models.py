from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')  # Image field

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.product.name}'

    class Meta:
        ordering = ['-created_at']

    def average_rating(self):
        reviews = Review.objects.filter(product=self.product)
        if reviews.exists():
            return sum(review.rating for review in reviews) / len(reviews)
        return 0

class Rate(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='rate')
    total_rates = models.PositiveIntegerField(default=0)
    total_stars = models.PositiveIntegerField(default=0)

    def update_rating(self, rating):
        self.total_rates += 1
        self.total_stars += rating
        self.save()

    def average_rating(self):
        if self.total_rates > 0:
            return self.total_stars / self.total_rates
        return 0
