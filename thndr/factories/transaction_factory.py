import factory.fuzzy

from thndr.models import Transaction
from thndr.factories.user_factory import UserFactory
from thndr.factories.stock_factory import StockFactory


class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction

    user = factory.SubFactory(UserFactory)
    stock = factory.SubFactory(StockFactory)

    amount = factory.Iterator([10, 3, 4])
    stocks_total = factory.Iterator([None, 3, 4])

    deposit = factory.Iterator([True, False, True])
    withdraw = factory.Iterator([False, True, False])
