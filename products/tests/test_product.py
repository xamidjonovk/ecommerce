from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from products.models import Product, Category, Review, User
from django.contrib.auth import get_user_model

User = get_user_model()


class ProductViewSetTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(phone_number='+998901234567', password='testpass')
        self.staff_user = User.objects.create_user(phone_number='+998997274760', password='staffpass', is_staff=True)

        self.category1 = Category.objects.create(name='Electronics')
        self.category2 = Category.objects.create(name='Books')

        self.product1 = Product.objects.create(name='Laptop', description='Powerful Laptop', category=self.category1, price=5000)
        self.product2 = Product.objects.create(name='Book', description='Thriller Book', category=self.category2, price=6000)

        Review.objects.create(product=self.product1, rating=5, user_id=1)
        Review.objects.create(product=self.product1, rating=4, user_id=2)
        Review.objects.create(product=self.product2, rating=2, user_id=1)

    def test_product_list(self):
        url = reverse('product-list')
        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)


    def test_product_filter_by_category(self):
        url = reverse('product-list') + '?category=' + str(self.category1.id)
        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)  # Should only have 1 product of the category 'Electronics'

    def test_product_detail(self):
        url = reverse('product-detail', args=[self.product1.id])
        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['product']['name'], 'Laptop')

    def test_top_rated(self):
        url = reverse('product-top-rated')
        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Laptop')

    def test_average_rating(self):
        url = reverse('product-average-rating', args=[self.product1.id])
        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['average_rating'], 4.5)  # (5+4) / 2

    def test_permission_denied_for_anonymous_create(self):
        self.client.force_authenticate(user=None)  # "Log out" to make the client anonymous
        url = reverse('product-list')
        data = {'name': 'Test Product', 'description': 'This is a test product', 'price': 10.00}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_permission_granted_for_staff(self):
        url = reverse('product-list')
        self.client.force_authenticate(self.staff_user)
        data = {'name': 'Test Product', 'description': 'This is a test product', 'price': 10.00}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
