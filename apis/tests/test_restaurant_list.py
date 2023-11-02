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

    def test_list(self):
        response = self.client.get(
            '/apiv1/restaurants/',
            )
        assert response.status_code == 200

        assert len(response.json()) == 3
        restaurant1 = response.json()[0]
        assert restaurant1['description'] == self.restaurant3.description
        assert restaurant1['id'] == self.restaurant3.id
        assert restaurant1['name'] == self.restaurant3.name
        assert restaurant1['image'] == '/avatar'
        assert restaurant1['status'] == self.restaurant3.status

        for restaurant in response.json():
            assert restaurant['id'] in [
                self.restaurant1.id,
                self.restaurant2.id,
                self.restaurant3.id,
            ]

