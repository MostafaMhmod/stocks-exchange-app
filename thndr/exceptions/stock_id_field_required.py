from rest_framework.exceptions import APIException


class StockIDFieldRequiredAPIException(APIException):
    status_code = 400
    default_detail = "Stock ID field required."
