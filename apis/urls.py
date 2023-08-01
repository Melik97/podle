from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apis.views.menus import MenusAPIView
from apis.views.restaurants import RestaurantAPIView

Default = DefaultRouter()
Default.register(r'restaurants', RestaurantAPIView, basename="restaurant")
Default.register(r'menus', MenusAPIView, basename="menu")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(Default.urls)),
    path(
        'restaurants/<str:restaurant_id>/menus',
        MenusAPIView.as_view({'get': 'retrieve', 'post': 'create'}),
        name='restaurant-menu'
    )
]

