from rest_framework import status
from rest_framework.test import APITestCase

from .models import Provider, GeoPolygon


class ProviderTestClass(APITestCase):
    """Test case for Creating Provider"""

    def setUp(self) -> None:
        self.data = {
            "name": "haseeb",
            "email": "haseeb@gmail.com",
            "language": "ENG",
            "phone_number": "03099106464",
            "currency": "USD"
        }

    def test_create_provider(self):
        url = '/provider/'
        response = self.client.post(path=url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_provider(self):
        invalid_data = {
            "name": 123,
            "email": 123,
            "language": 123,
            "phone_number": 12,
            "currency": "USD"

        }
        url = '/provider/'
        response = self.client.post(path=url, data=invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class SpecificProviderTestCase(APITestCase):
    """ Test Case for Specific Provider"""

    def setUp(self) -> None:
        self.user = Provider.objects.create(
            name='test',
            email='test@gmail.com',
            language='ENG',
            phone_number='0309910654',
            currency="USD"

        )

    def test_get_api(self):
        url = f'/provider/{self.user.id}/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_specific_provider_with_invalid_id(self) -> None:
        # testing with invalid Task ID

        url = '/provider/10/'
        get_response = self.client.get(path=url)
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)


class UpdateProviderTestCase(APITestCase):
    """Test Case for Updating Provider"""

    def setUp(self) -> None:
        self.data = {
            "name": "haseeb",
            "email": "haseeb@gmail.com",
            "language": "ENG",
            "phone_number": "03099106464",
            "currency": "USD"

        }

        self.user = Provider.objects.create(
            name='test',
            email='test@gmail.com',
            language='ENG',
            phone_number='03099106544',
            currency="USD"

        )

    def test_update_provider(self):
        url = f'/provider/{self.user.id}/'
        response = self.client.put(path=url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_with_invalid_id(self) -> None:
        url = '/provider/100/'
        test_data = {
            "name": "haseeb",
            "email": "haseeb@gmail.com",
            "language": "ENG",
            "phone_number": "03099106464",
            "currency": "USD"
        }

        update_response = self.client.put(
            path=url, data=test_data)
        self.assertEqual(update_response.status_code,
                         status.HTTP_404_NOT_FOUND)


class DeleteTestCase(APITestCase):
    """ Test  Case for delete Provider"""

    def setUp(self) -> None:
        self.user = Provider.objects.create(
            name='test',
            email='test@gmail.com',
            language='ENG',
            phone_number='0309910654',
            currency="USD"
        )

    def test_delete_provider(self):
        url = f'/provider/{self.user.id}/'
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_id_delete(self) -> None:
        url = '/provider/100/'
        get_response = self.client.delete(path=url)
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)


class GetProviderListTestCase(APITestCase):
    """ Test Case for Get Provider List"""

    def setUp(self) -> None:
        self.user = Provider.objects.create(
            name='test',
            email='test@gmail.com',
            language='ENG',
            phone_number='03099106544',
            currency="USD"
        )

    def test_get_all(self):
        url = '/provider/'
        get_response = self.client.get(path=url)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)


class PolyGonTestClass(APITestCase):
    """Test case for Creating Polygon"""

    def setUp(self) -> None:
        self.user = Provider.objects.create(
            name='test',
            email='test@gmail.com',
            language='ENG',
            phone_number='03099106544',
            currency="USD"
        )

        self.data = {
            "provider": self.user.id,
            "polygon_name": "Triangle",
            "price": "1000.0",
            "poly": "POLYGON((0 0, 0 10, 10 10, 0 0))",

        }

    def test_create_polygon(self):
        url = '/geopolygon/'
        response = self.client.post(path=url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_provider(self):
        invalid_data = {
            "provider": 1000,
            "polygon_name": "Triangle",
            "price": "1000.0",
            "poly": "POLYGON((0 0, 0 10, 10 10, 0 0))",

        }

        url = '/geopolygon/'
        response = self.client.post(path=url, data=invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class SpecificPolyGonTestCase(APITestCase):
    """ Test Case for Specific Polygon"""

    def setUp(self) -> None:
        self.user = Provider.objects.create(
            name='test',
            email='test@gmail.com',
            language='ENG',
            phone_number='03099106544',
            currency="USD"
        )

        self.data = GeoPolygon.objects.create(
            provider=self.user,
            polygon_name='Triangle',
            price='1000.0',
            poly="POLYGON((0 0, 0 10, 10 10, 0 0))",

        )

    def test_get_specific_polygon(self):
        url = f'/geopolygon/{self.data.id}/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
