from rest_framework.exceptions import APIException


class ValidTotalFieldRequiredAPIException(APIException):
    status_code = 400
    default_detail = "A valid total buy order is required."
