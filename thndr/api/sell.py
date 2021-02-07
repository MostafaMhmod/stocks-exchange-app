
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ParseError, NotFound
from thndr.exceptions.stock_id_field_required import \
    StockIDFieldRequiredAPIException
from thndr.exceptions.user_id_field_required import \
    UserIDFieldRequiredAPIException
from thndr.exceptions.valid_total_field_required import \
    ValidTotalFieldRequiredAPIException
from thndr.exceptions.price_out_of_bounds import \
    PriceOutOfBoundsAPIException
from thndr.models import Holding, Stock, Wallet
from thndr.serializers.holding_serializer import HoldingWriteSerializer
from thndr.serializers.wallet_serializers import WalletWriteSerializer
from thndr.utils.buy_and_sell_validations import validate_action


@api_view(["POST"])
def sell(request):
    validate_action(request.data)

    user_id = request.data["user_id"]
    stock_id = request.data["stock_id"]
    total_sell_order = request.data["total"]
    upper_bound = request.data["upper_bound"]
    lower_bound = request.data["lower_bound"]

    holding_data = {}
    wallet_data = {}
    wallet = None
    stock = None

    try:
        total_sell_order = int(total_sell_order)
        upper_bound = int(upper_bound)
        lower_bound = int(lower_bound)
    except ValueError:
        raise ParseError

    try:
        wallet = Wallet.objects.get(user__pk=user_id)
        stock = Stock.objects.get(stock_uuid=stock_id)
    except Wallet.DoesNotExist:
        raise UserIDFieldRequiredAPIException
    except Stock.DoesNotExist:
        raise StockIDFieldRequiredAPIException

    # Check if user have enough balance
    if not total_sell_order <= wallet.balance and total_sell_order <= stock.quantity:
        raise ValidTotalFieldRequiredAPIException

    # check if price match
    if stock.price < lower_bound or stock.price > upper_bound:
        raise PriceOutOfBoundsAPIException

    # if a holding with that stock already exists, update the existing holding and update the wallet
    try:
        holding = Holding.objects.get(user__pk=user_id, stock__stock_uuid=stock_id)
        holding_data['user'] = user_id
        holding_data['stock'] = stock.pk
        holding_data['quantity'] = holding.quantity - total_sell_order

        # removing stocks

        serializer = HoldingWriteSerializer(holding, data=holding_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # adding money to wallet balance
        wallet_data['balance'] = wallet.balance + total_sell_order

        serializer = WalletWriteSerializer(wallet, data=wallet_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    # if no holding with that stock already exists, raise NotFound Exception
    except Holding.DoesNotExist:
        raise NotFound

    return Response({"success": True})
