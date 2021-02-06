from rest_framework.exceptions import APIException


class AmountFieldRequiredAPIException(APIException):
    status_code = 400
    default_detail = "Amount field required."
