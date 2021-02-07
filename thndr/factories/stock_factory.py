import factory.fuzzy
from thndr.models import Stock


class StockFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Stock

    name = factory.Sequence(lambda n: "Name-%d" % n)
    price = factory.Iterator([1, 3, 4])
    quantity = factory.Iterator([5, 6, 7])
