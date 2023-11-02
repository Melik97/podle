from rest_framework.exceptions import APIException


class StatusRestaurantNameIsExist(APIException):
    status_code = 400
    default_detail = 'Restaurant Name Is Exist'
    default_code = '1000'


class StatusRestaurantDoesNotExist(APIException):
    status_code = 400
    default_detail = 'Restaurant Does Not Exist'
    default_code = '1001'


class StatusMenuDoesNotExist(APIException):
    status_code = 400
    default_detail = 'Menu Does Not Exist'
    default_code = '1002'


class StatusMenuIsExist(APIException):
    status_code = 400
    default_detail = 'Menu Is Exist'
    default_code = '1003'


class StatusCategoryIsExist(APIException):
    status_code = 400
    default_detail = 'Category Is Exist'
    default_code = '1003'


class HTTPNotFound(APIException):
    status_code = 404
    default_detail = '404 Not Found'

