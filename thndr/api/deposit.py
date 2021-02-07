
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from thndr.exceptions.amount_field_is_int import AmountFieldIsIntAPIException
from thndr.exceptions.amount_field_required import \
    AmountFieldRequiredAPIException
from thndr.exceptions.user_id_field_required import \
    UserIDFieldRequiredAPIException
from thndr.models import Wallet
from thndr.serializers.wallet_serializers import WalletWriteSerializer


@api_view(["PUT"])
def deposit(request):
    user_id = request.data["user_id"]
    amount = request.data["amount"]

    if not user_id:
        raise UserIDFieldRequiredAPIException

    if not amount:
        raise AmountFieldRequiredAPIException

    try:
        amount = int(amount)
    except ValueError:
        raise AmountFieldIsIntAPIException

    wallet = get_object_or_404(Wallet, user__pk=user_id)

    wallet__balance = wallet.balance

    request.data["balance"] = wallet__balance + amount

    serializer = WalletWriteSerializer(wallet, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response({"success": True})
