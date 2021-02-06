from rest_framework.exceptions import APIException


class NegativeBalanceAPIException(APIException):
    status_code = 400
    default_detail = "balance cant be negative."
