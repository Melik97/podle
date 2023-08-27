from rest_framework.test import APITestCase

from apis.models.restaurant import Restaurant


class TestRestaurant(APITestCase):
    @classmethod
    def setUp(cls):
        cls.restaurant1 = Restaurant(
            name='name 1',
            description='description',
            image='image',
            status=True,
        )
        cls.restaurant1.save()

    def test_list(self):
        response = self.client.patch(
            f'/apiv1/restaurants/{self.restaurant1.id}/',
            data={
                'name': 'new name',
            }
        )
        assert response.status_code == 200
        assert response.json()['id'] == self.restaurant1.id
        assert response.json()['name'] == 'new name'
        assert response.json()['description'] == self.restaurant1.description

        response = self.client.patch(
            f'/apiv1/restaurants/{self.restaurant1.id}/',
            data={
                'name': 'new name 2',
                'description': 'new description 2',
            }
        )
        assert response.status_code == 200
        assert response.json()['id'] == self.restaurant1.id
        assert response.json()['name'] == 'new name 2'
        assert response.json()['description'] == 'new description 2'

        response = self.client.delete(
            f'/apiv1/restaurants/0/',
        )
        assert response.status_code == 400
        assert response.json()['detail'] == 'Restaurant Does Not Exist'

        response = self.client.get(
            f'/apiv1/restaurants/a/',
        )
        assert response.status_code == 404
        assert response.json()['detail'] == '404 Not Found'

