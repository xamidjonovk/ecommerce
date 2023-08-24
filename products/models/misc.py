from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from .product import Product


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    rating = models.PositiveIntegerField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.rating}"


class FlashSale(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    discount_percentage = models.PositiveIntegerField()  # e.g., 20 means 20% off
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def is_active(self):
        now = timezone.now()
        return self.start_time <= now <= self.end_time

    class Meta:
        unique_together = ('product', 'start_time', 'end_time')


class ProductViewHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)