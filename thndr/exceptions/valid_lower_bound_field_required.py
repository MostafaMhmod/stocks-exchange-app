from rest_framework.exceptions import APIException


class ValidLowerBoundFieldRequiredAPIException(APIException):
    status_code = 400
    default_detail = "A valid lower bound is required."
