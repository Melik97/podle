from rest_framework.test import APITestCase, Tran


class TestRestaurant(APITestCase):
    def setUp(self):
        pass

    def test_create(self):
        response = self.client.post(
            '/apiv1/restaurants/',
            data={
                'name': 'restaurant1',
                'description': 'restaurant1 descriptions',
                'image': 'avatar',
                'status': True,
            },
        )
        assert response.status_code == 200

        response = self.client.post(
            '/apiv1/restaurants/',
            data={
                'name': 'restaurant1',
                'description': 'restaurant1 descriptions',
                'image': 'avatar',
                'status': True,
            },
        )
        assert response.status_code == 400
        assert response.json()['detail'] == 'Restaurant Name Is Exist'

