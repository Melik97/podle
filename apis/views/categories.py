from rest_framework import viewsets
from rest_framework.response import Response

from apis.celery_tasks import create_menu
from apis.exceptions import StatusRestaurantDoesNotExist, StatusCategoryIsExist
from apis.models.category import Category
from apis.models.restaurant import Restaurant
from apis.serilizers.categories import CategorySerializer


class CategoriesAPIView(viewsets.ViewSet):

    @staticmethod
    def list(request, restaurant_id):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response({'categories': serializer.data})

    @staticmethod
    def create(request, restaurant_id):
        data = request.data
        restaurant = Restaurant.objects.filter(pk=restaurant_id).first()
        if restaurant is None:
            raise StatusRestaurantDoesNotExist()

        is_exist = Category.objects.filter(name=data['name']).first()
        if is_exist is not None:
            raise StatusCategoryIsExist()

        category = Category.objects.create(
            name=data['name'],
        )
        create_menu.delay(
            name=data['name'],
            restaurant_id=restaurant_id
        )
        serializer = CategorySerializer(category)
        return Response(serializer.data)

