
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from thndr.serializers.stock_serializer import StockRetrieveSerializer
from thndr.models import Stock


@api_view(["GET"])
def stock(request):
    stock_uuid = request.data.get('stock_id')
    try:
        queryset = Stock.objects.get(stock_uuid=stock_uuid)
    except Exception:
        raise NotFound

    serializer = StockRetrieveSerializer(queryset)

    return Response(serializer.data)
