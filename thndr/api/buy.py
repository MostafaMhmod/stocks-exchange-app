
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
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
from thndr.utils.buy_and_sell_validations import validate_action


@api_view(["POST"])
def buy(request):
    validate_action(request.data)

    user_id = request.data["user_id"]
    stock_id = request.data["stock_id"]
    total_buy_order = request.data["total"]
    upper_bound = request.data["upper_bound"]
    lower_bound = request.data["lower_bound"]

    data = {}
    wallet = None
    stock = None

    try:
        total_buy_order = int(total_buy_order)
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
    if not total_buy_order <= wallet.balance and total_buy_order <= stock.quantity:
        raise ValidTotalFieldRequiredAPIException

    # check if price match
    if stock.price < lower_bound or stock.price > upper_bound:
        raise PriceOutOfBoundsAPIException

    # if a holding with that stock already exists, update the existing holding
    try:
        holding = Holding.objects.get(user__pk=user_id, stock__stock_uuid=stock_id)
        data['user'] = user_id
        data['stock'] = stock.pk
        data['quantity'] = holding.quantity + total_buy_order

        serializer = HoldingWriteSerializer(holding, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    # if no holding with that stock already exists, create a holding
    except Holding.DoesNotExist:
        serializer = HoldingWriteSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    return Response({"success": True})
