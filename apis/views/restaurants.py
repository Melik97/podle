from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from apis.exceptions import StatusRestaurantNameIsExist, \
    StatusRestaurantDoesNotExist
from apis.helpers import int_or_notfound
from apis.models.restaurant import Restaurant
from apis.serilizers.serializers import RestaurantSerializer


class RestaurantAPIView(viewsets.ViewSet):

    @staticmethod
    def list(request):
        queryset = Restaurant.objects.all()
        serializer = RestaurantSerializer(queryset, many=True)
        return Response(serializer.data)

    @staticmethod
    def create(request):
        data = request.data
        is_exist = Restaurant.objects.filter(name=data['name']).first()
        if is_exist is not None:
            raise StatusRestaurantNameIsExist()

        restaurant = Restaurant.objects.create(
            name=data['name'],
            description=data['description'],
            image=data['image'],
            status=data['status'],
        )
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    @staticmethod
    def delete(request, pk):
        pk = int_or_notfound(pk)
        restaurant = get_object_or_404(Restaurant, pk=pk)
        restaurant.delete()
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    @staticmethod
    def get(request, pk=None):
        pk = int_or_notfound(pk)
        restaurant = get_object_or_404(Restaurant, pk=pk)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    @staticmethod
    def partial_update(request, pk):
        pk = int_or_notfound(pk)
        restaurant = get_object_or_404(Restaurant, pk=pk)
        if restaurant is None:
            raise StatusRestaurantDoesNotExist()

        serializer = RestaurantSerializer(
            restaurant,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

