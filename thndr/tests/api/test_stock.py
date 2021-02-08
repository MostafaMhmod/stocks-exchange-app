from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from thndr.factories.user_factory import UserFactory
from thndr.factories.stock_factory import StockFactory
from thndr.factories.transaction_factory import TransactionFactory
from thndr.tests.base_api_test_case import BaseAPITestCase


class StockTestCase(APITestCase, BaseAPITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.stock = StockFactory(price=5)
        cls.stock_path = reverse("stock")
        cls.data = {
            "stock_id": cls.stock.stock_uuid,
        }

    def test_stock_retreive(self):
        self.post(self.stock_path, status_code=200, data=self.data, format="json")

    def test_stock_retreive_fails_if_id_doesnt_exist(self):
        data = self.data.copy()
        data['stock_id'] = 200
        self.post(self.stock_path, status_code=404, data=data, format="json")
