from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from thndr.factories.user_factory import UserFactory
from thndr.factories.stock_factory import StockFactory
from thndr.factories.transaction_factory import TransactionFactory
from thndr.tests.base_api_test_case import BaseAPITestCase


class SellTestCase(APITestCase, BaseAPITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.stock = StockFactory(price=5)
        # adding 2 transactions, one for deposit and one for buying the stock
        cls.transaction1 = TransactionFactory(user=cls.user, amount=cls.stock.price,
                                              stock=None, deposit=True, withdraw=False)
        cls.transaction2 = TransactionFactory(user=cls.user, stock=cls.stock, stocks_total=1,
                                              amount=cls.stock.price * 1, deposit=True, withdraw=False)
        cls.withdraw_path = reverse("account-withdraw")
        cls.deposit_path = reverse("account-deposit")
        cls.buy_path = reverse("stock-buy")
        cls.sell_path = reverse("stock-sell")
        cls.data = {
            "user_id": cls.user.pk,
            "stock_id": cls.stock.stock_uuid,
            "total": 1,
            "upper_bound": cls.stock.price,
            "lower_bound": 1
        }

    def test_sell_stock_for_user_with_stock(self):
        self.post(self.sell_path, status_code=200, data=self.data, format="json")

    def test_sell_fails_if_user_had_non_of_the_stock(self):
        stock = StockFactory()
        data = self.data.copy()
        data['stock_id'] = stock.pk
        self.post(self.sell_path, status_code=400, data=data, format="json")

    def test_sell_fails_if_theres_no_matchin_stock(self):
        data = self.data.copy()
        data['stock_id'] = "32"
        self.post(self.sell_path, status_code=400, data=data, format="json")

    def test_sell_fails_if_body_isnt_correct(self):
        data = self.data.copy()
        data['upper_bound'] = "32"
        data['lower_bound'] = "32"
        self.post(self.sell_path, status_code=400, data=data, format="json")

    def test_sell_fails_if_stock_price_out_of_user_price_bounds(self):
        data = self.data.copy()
        data['upper_bound'] = 1000
        data['lower_bound'] = 10
        self.post(self.sell_path, status_code=400, data=data, format="json")
