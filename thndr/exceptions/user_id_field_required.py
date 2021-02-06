from rest_framework.exceptions import APIException


class UserIDFieldRequiredAPIException(APIException):
    status_code = 400
    default_detail = "User ID field required."
