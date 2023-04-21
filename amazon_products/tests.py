from django.test import TestCase
from rest_framework.test import APIClient
from .models import Producto
from .serializers import ProductoSerializer
import datetime

class ProductoAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        # Crea un producto de ejemplo en la base de datos
        self.producto = Producto.objects.create(
            fecha=datetime.date(2023, 4, 21),
            imagen="https://example.com/image.jpg",
            nombre="Producto de prueba",
            distribuidor="Distribuidor de prueba",
            ASIN="B08EXAMPLE",
            precio=15.0,
            EAN="1234567890123"
        )

    def test_create_producto(self):
        url = "/amazon/api/v1/productos/"
        data = {
            "fecha": "21-04-2023",
            "imagen": "https://example.com/image2.jpg",
            "nombre": "Producto de prueba 2",
            "distribuidor": "Distribuidor de prueba 2",
            "ASIN": "B08EXAMPLE2",
            "precio": 25.0,
            "EAN": "2345678901234"
        }

        response = self.client.post(url, data, format='json')
        if response.status_code != 201:
            print("Error al crear producto:", response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Producto.objects.count(), 2)
        self.assertEqual(Producto.objects.get(pk=response.data['id']).nombre, data['nombre'])

    def test_invalid_date_format(self):
        url = "/amazon/api/v1/productos/"
        data = {
            "fecha": "21/04/2023",
            "imagen": "https://example.com/image2.jpg",
            "nombre": "Producto de prueba 2",
            "distribuidor": "Distribuidor de prueba 2",
            "ASIN": "B08EXAMPLE2",
            "precio": 25.0,
            "EAN": "2345678901234"
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("Error al analizar la fecha", response.data['fecha'][0])

