from rest_framework.exceptions import APIException


class AmountFieldIsIntAPIException(APIException):
    status_code = 400
    default_detail = "Amount field must be a number."
