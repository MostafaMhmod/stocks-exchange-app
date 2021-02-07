
from rest_framework.decorators import api_view
from rest_framework.response import Response
from thndr.exceptions.amount_field_required import \
    AmountFieldRequiredAPIException
from thndr.exceptions.user_id_field_required import \
    UserIDFieldRequiredAPIException
from thndr.serializers.transaction_serializer import TransactionCreateSerializer


@api_view(["POST"])
def withdraw(request):
    if 'user_id' not in request.data:
        raise UserIDFieldRequiredAPIException
    if 'amount' not in request.data:
        raise AmountFieldRequiredAPIException

    data = {}

    data['user'] = request.data['user_id']
    data['amount'] = request.data['amount']
    data['is_wallet'] = True
    data['is_stock'] = False
    data['is_withdraw'] = True
    data['is_deposit'] = False

    serializer = TransactionCreateSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response({"success": True})
