from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response

from apis.exceptions import StatusMenuDoesNotExist, StatusMenuIsExist, \
    StatusRestaurantDoesNotExist
from apis.helpers import int_or_notfound
from apis.models.menu import Menu
from apis.models.menu_restaurant import MenuRestaurant
from apis.models.restaurant import Restaurant
from apis.serilizers.menus import MenuSerializer


# class MenusAPIView(mixins.CreateModelMixin, mixins.UpdateModelMixin,
#                    generics.GenericAPIView):
class MenusAPIView(viewsets.ViewSet):

    def create(self, request, *args, **kwargs):
        pass

    @staticmethod
    def retrieve(request, restaurant_id):
        menu = Menu.objects.get(restaurant=restaurant_id)
        if menu is None:
            raise StatusMenuDoesNotExist()

        serializer = MenuSerializer(menu)
        return Response(serializer.data)

    @staticmethod
    def list(request):
        queryset = Menu.objects.all()
        serializer = MenuSerializer(queryset, many=True)
        return Response({'menus': serializer.data})

    # @staticmethod
    # def create(request, restaurant_id):
    #     data = request.data
    #     restaurant = Restaurant.objects.filter(pk=restaurant_id).first()
    #     if restaurant is None:
    #         raise StatusRestaurantDoesNotExist()
    #
    #     is_exist = Menu.objects.filter(restaurant_id=restaurant_id).first()
    #     if is_exist is not None:
    #         raise StatusMenuIsExist()
    #
    #     menu = Menu.objects.create(
    #         name=data['name'],
    #         description=data['description'],
    #         image=data['image'],
    #         restaurant_id=restaurant.pk,
    #     )
    #     serializer = MenuSerializer(menu)
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
