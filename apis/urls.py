from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apis.views import RestaurantAPIView

restaurants = DefaultRouter()
restaurants.register(
    r'restaurants',
    RestaurantAPIView,
    basename="restaurants"
    )

# restaurants.register(
#     r'restaurants/<str:pk>',
#     RestaurantAPIView,
#     basename="restaurant"
#     )


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(restaurants.urls)),
]