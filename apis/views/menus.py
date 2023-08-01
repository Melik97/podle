from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from apis.exceptions import StatusRestaurantNameIsExist, \
    StatusRestaurantDoesNotExist
from apis.helpers import int_or_notfound
from apis.models.menu import Menu
from apis.models.restaurant import Restaurant
from apis.serilizers.menus import MenuSerializer
from apis.serilizers.serializers import RestaurantSerializer


class MenusAPIView(viewsets.ViewSet):

    @staticmethod
    def retrieve(request, restaurant_id):
        menu = Menu.objects.get(restaurant_id=restaurant_id)
        if menu is None:
            raise StatusRestaurantDoesNotExist()

        serializer = MenuSerializer(menu)
        return Response(serializer.data)

    @staticmethod
    def list(request):
        print(request.GET.urlencode())
        queryset = Menu.objects.all()
        serializer = MenuSerializer(queryset, many=True)
        return Response({'menus': serializer.data})

    # @staticmethod
    # def create(request):
    #     data = request.data
    #     is_exist = Restaurant.objects.filter(name=data['name']).first()
    #     if is_exist is not None:
    #         raise StatusRestaurantNameIsExist()
    #
    #     restaurant = Restaurant.objects.create(
    #         name=data['name'],
    #         description=data['description'],
    #         image=data['image'],
    #         status=data['status'],
    #     )
    #     serializer = RestaurantSerializer(restaurant)
    #     return Response(serializer.data)
    #
    # @staticmethod
    # def delete(request, pk):
    #     pk = int_or_notfound(pk)
    #     restaurant = Restaurant.objects.filter(pk=pk).first()
    #     if restaurant is None:
    #         raise StatusRestaurantDoesNotExist()
    #
    #     restaurant.delete()
    #     serializer = RestaurantSerializer(restaurant)
    #     return Response(serializer.data)
    #
    # @staticmethod
    # def get(request, pk=None):
    #     pk = int_or_notfound(pk)
    #     restaurant = Menu.objects.filter(pk=pk).first()
    #     if restaurant is None:
    #         raise StatusRestaurantDoesNotExist()
    #
    #     serializer = RestaurantSerializer(restaurant)
    #     return Response(serializer.data)
    #
    # @staticmethod
    # def partial_update(request, pk):
    #     pk = int_or_notfound(pk)
    #     restaurant = Restaurant.objects.filter(pk=pk).first()
    #     if restaurant is None:
    #         raise StatusRestaurantDoesNotExist()
    #
    #     serializer = RestaurantSerializer(
    #         restaurant,
    #         data=request.data,
    #         partial=True
    #     )
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
