from rest_framework.test import APITestCase

from apis.models.restaurant import Restaurant


class TestRestaurant(APITestCase):
    @classmethod
    def setUp(cls):
        cls.restaurant_1 = Restaurant(
            name='name 1',
            description='description',
            image='image',
            status=True,
        )
        cls.restaurant_1.save()

        cls.restaurant_2 = Restaurant(
            name='name 2',
            description='description',
            image='image',
            status=True,
        )
        cls.restaurant_2.save()

        cls.restaurant_3 = Restaurant(
            name='name 3',
            description='description',
            image='image',
            status=True,
        )
        cls.restaurant_3.save()

    def test_delete(self):
        response = self.client.get(f'/apiv1/restaurants/')
        assert response.status_code == 200
        assert len(response.json()) == 3

        response = self.client.delete(
            f'/apiv1/restaurants/{self.restaurant_2.id}/',
        )
        assert response.status_code == 200
        assert response.json()['id'] is None
        assert response.json()['name'] == self.restaurant_2.name

        response = self.client.get(f'/apiv1/restaurants/')
        assert response.status_code == 200
        assert len(response.json()) == 2

        response = self.client.delete(
            f'/apiv1/restaurants/{self.restaurant_2.id}/',
        )
        assert response.status_code == 400
        assert response.json()['detail'] == 'Restaurant Does Not Exist'

        response = self.client.get(
            f'/apiv1/restaurants/a/',
        )
        assert response.status_code == 404
        assert response.json()['detail'] == '404 Not Found'
