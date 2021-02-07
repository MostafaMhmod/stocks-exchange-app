
from rest_framework.decorators import api_view
from rest_framework.response import Response
from thndr.serializers.transaction_serializer import TransactionStockCreateSerializer, TransactionWalletCreateSerializer


@api_view(["POST"])
def buy(request):
    # 1st transaction to add the stock transaction
    data = {}

    data['user'] = request.data.get("user_id")
    data['stock'] = request.data.get("stock_id")
    data['stocks_total'] = request.data.get('total')
    data['withdraw'] = False
    data['deposit'] = True

    serializer = TransactionStockCreateSerializer(data=data)
    serializer.context['upper_bound'] = request.data.get('upper_bound')
    serializer.context['lower_bound'] = request.data.get('lower_bound')

    serializer.is_valid(raise_exception=True)
    output = serializer.save()

    # 2nd transaction to remove total cost from the user balance
    data = {}

    data['user'] = output.user.pk
    data['amount'] = output.amount
    data['withdraw'] = True
    data['deposit'] = False

    serializer = TransactionWalletCreateSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response({"success": True})
