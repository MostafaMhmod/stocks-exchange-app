import factory.fuzzy
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from thndr.models import Transaction
from thndr.factories.stock_factory import StockFactory
from thndr.tests.base_api_test_case import BaseAPITestCase


class DepositTestCase(APITestCase, BaseAPITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.stock = StockFactory()

    def test_stock_created(self):
        self.assertTrue(self.stock.pk)
