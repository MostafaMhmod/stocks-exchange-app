from thndr.exceptions.user_id_field_required import \
    UserIDFieldRequiredAPIException
from thndr.exceptions.stock_id_field_required import \
    StockIDFieldRequiredAPIException
from thndr.exceptions.valid_total_field_required import \
    ValidTotalFieldRequiredAPIException
from thndr.exceptions.valid_upper_bound_field_required import \
    ValidUpperBoundFieldRequiredAPIException
from thndr.exceptions.valid_lower_bound_field_required import \
    ValidLowerBoundFieldRequiredAPIException


def validate_action(data):
    if 'user_id' not in data:
        raise UserIDFieldRequiredAPIException
    if 'stock_id' not in data:
        raise StockIDFieldRequiredAPIException
    if 'total' not in data:
        raise ValidTotalFieldRequiredAPIException
    if 'upper_bound' not in data:
        raise ValidUpperBoundFieldRequiredAPIException
    if 'lower_bound' not in data:
        raise ValidLowerBoundFieldRequiredAPIException
