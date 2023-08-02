# Create your tasks here

from celery import shared_task

from apis.serilizers.menus import MenuSerializer


@shared_task()
def create_menu(name, restaurant_id):
    MenuSerializer.create(
        validated_data=dict(
            name=name,
            restaurant_id=restaurant_id
        )
    )
    print('done')

