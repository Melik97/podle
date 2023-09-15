from rest_framework.test import APITestCase

from apis.models.restaurant import Restaurant


class TestRestaurant(APITestCase):

    @classmethod
    def setUp(cls):
        cls.restaurant1 = Restaurant(
            name='restaurant1',
            description='restaurant1 descriptions',
            image='avatar',
            status=True,
        )
        cls.restaurant1.save()

        cls.restaurant2 = Restaurant(
            name='restaurant2',
            description='restaurant2 descriptions',
            image='avatar',
            status=True,
        )
        cls.restaurant2.save()

        cls.restaurant3 = Restaurant(
            name='restaurant3',
            description='restaurant3 descriptions',
            image='avatar',
            status=True,
        )
        cls.restaurant3.save()

    def test_get(self):
        response = self.client.get(
            f'/apiv1/restaurants/{self.restaurant2.id}/',
        )
        assert response.status_code == 200
        assert response.json()['id'] == self.restaurant2.id
        assert response.json()['name'] == self.restaurant2.name

        response = self.client.get(
            f'/apiv1/restaurants/0/',
        )
        assert response.status_code == 404

        response = self.client.get(
            f'/apiv1/restaurants/a/',
        )
        assert response.status_code == 404
        assert response.json()['detail'] == '404 Not Found'

