from rest_framework import serializers

from apis.models.category import Category
from apis.models.menu import Menu
from apis.serilizers.categories import CategorySerializer


class MenuSerializer(serializers.ModelSerializer):

    @staticmethod
    def create(validated_data):
        category = Category.objects.get(name=validated_data.get('name'))
        validated_data['category'] = category
        return Menu.objects.create(**validated_data)

    class Meta:
        model = Menu
        fields = '__all__'

