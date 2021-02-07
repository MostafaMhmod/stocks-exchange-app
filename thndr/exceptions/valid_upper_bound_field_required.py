from rest_framework.exceptions import APIException


class ValidUpperBoundFieldRequiredAPIException(APIException):
    status_code = 400
    default_detail = "A valid upper bound is required."
