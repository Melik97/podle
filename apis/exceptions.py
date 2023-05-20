from rest_framework.exceptions import APIException


class StatusRestaurantNameIsExist(APIException):
    status_code = 400
    default_detail = 'Restaurant Name Is Exist'
    default_code = '1000'


class StatusRestaurantDoesNotExist(APIException):
    status_code = 400
    default_detail = 'Restaurant Does Not Exist'
    default_code = '1001'


class HTTPNotFound(APIException):
    status_code = 404
    default_detail = '404 Not Found'

