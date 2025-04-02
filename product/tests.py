from django.test import TestCase, Client
from rest_framework.test import APIClient
from django.urls import reverse_lazy
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .models import ProductCategory, ProductTag
User = get_user_model()
from django.conf import settings
import os

# Create your tests here.

class TestProductApi(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = reverse_lazy('products')
        user = User.objects.create_user(username='john', email='js@js.com', password='js.sj')
        cls.client = APIClient()
        refresh = RefreshToken.for_user(user)
        cls.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        category = ProductCategory.objects.create(title = 'Category #1')
        tag = ProductTag.objects.create(title = 'Tag #1')
        file_path = os.path.join(settings.MEDIA_ROOT, 'product_images/bowl-3.png')
        cls.data = {
            'title' : 'Product #1',
            'category' : category.id,
            'tags' : tag.id,
            'description' : 'sample description',
            'quantity' : 10,
            'cover_image' : (open(file_path, 'rb'),),
            'price' : 100,
        }
        cls.post_valid = cls.client.post(cls.url, data = cls.data)

    def test_product_api_url(self):
        self.assertEqual(self.url, '/en/api/products/')

    def test_product_create_status(self):
        self.assertEqual(self.post_valid.status_code, 201)

    def test_response_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    @classmethod
    def tearDownClass(cls):
        pass