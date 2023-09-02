from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from products.models import Order
from products.models import Review, Category
from products.permissions import IsOwnerOrReadOnly
from products.serializers import OrderSerializer
from products.serializers import ReviewSerializer, CategorySerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  # default =  AllowAny

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
