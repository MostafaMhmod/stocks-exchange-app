from rest_framework.exceptions import APIException


class PriceOutOfBoundsAPIException(APIException):
    status_code = 400
    default_detail = "Price is not in the lower and upper bounds"
