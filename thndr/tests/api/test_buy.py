from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from thndr.factories.user_factory import UserFactory
from thndr.factories.stock_factory import StockFactory
from thndr.factories.transaction_factory import TransactionFactory
from thndr.tests.base_api_test_case import BaseAPITestCase


class BuyTestCase(APITestCase, BaseAPITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.stock = StockFactory(price=5)
        cls.transaction = TransactionFactory(user=cls.user, amount=cls.stock.price,
                                             stock=None, deposit=True, withdraw=False)
        cls.withdraw_path = reverse("account-withdraw")
        cls.deposit_path = reverse("account-deposit")
        cls.buy_path = reverse("stock-buy")
        cls.data = {
            "user_id": cls.user.pk,
            "stock_id": cls.stock.stock_uuid,
            "total": 1,
            "upper_bound": cls.stock.price,
            "lower_bound": 1
        }

    def test_buy_stock_for_user_with_balance(self):
        self.post(self.buy_path, status_code=200, data=self.data, format="json")

    def test_buy_fails_if_user_had_no_balance(self):
        user = UserFactory()
        data = self.data.copy()
        data['user_id'] = user.pk
        self.post(self.buy_path, status_code=400, data=data, format="json")

    def test_buy_fails_if_theres_no_matchin_stock(self):
        data = self.data.copy()
        data['stock_id'] = "32"
        self.post(self.buy_path, status_code=400, data=data, format="json")

    def test_buy_fails_if_body_isnt_correct(self):
        data = self.data.copy()
        data['upper_bound'] = "32"
        data['lower_bound'] = "32"
        self.post(self.buy_path, status_code=400, data=data, format="json")

    def test_buy_fails_if_stock_price_out_of_user_price_bounds(self):
        data = self.data.copy()
        data['upper_bound'] = 1000
        data['lower_bound'] = 10
        self.post(self.buy_path, status_code=400, data=data, format="json")
