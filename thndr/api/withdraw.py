
from rest_framework.decorators import api_view
from rest_framework.response import Response
from thndr.serializers.transaction_serializer import TransactionWalletCreateSerializer


@api_view(["POST"])
def withdraw(request):
    data = {}

    data['user'] = request.data.get('user_id')
    data['amount'] = request.data.get('amount')
    data['withdraw'] = True
    data['deposit'] = False

    serializer = TransactionWalletCreateSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response({"success": True})
