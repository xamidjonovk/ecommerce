from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from products.models import Order, Product


class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'product', 'customer', 'quantity', 'created_at', 'total_price', 'phone_number', 'is_paid']

    def get_total_price(self, obj):
        return obj.product.price * obj.quantity

    def validate_quantity(self, value):
        try:
            # Fetch the product instance from the database
            product_id = self.initial_data['product']
            product = Product.objects.get(id=product_id)

            # Check the stock
            if value > product.stock:
                raise serializers.ValidationError("Not enough items in stock.")

            if value < 1:
                raise serializers.ValidationError("Quantity must be at least 1.")

            return value

        except ObjectDoesNotExist:
            raise serializers.ValidationError("Product does not exist")

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        product = order.product
        product.stock -= order.quantity
        product.save()
        self.send_confirmation_email(order)
        return order

    def send_confirmation_email(self, order):
        # Here you would send an email. For this example, we'll just print
        print(f"Sent confirmation email for Order {order.id}")
