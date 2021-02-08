from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from thndr.factories.user_factory import UserFactory
from thndr.factories.stock_factory import StockFactory
from thndr.factories.transaction_factory import TransactionFactory
from thndr.tests.base_api_test_case import BaseAPITestCase


class UserTestCase(APITestCase, BaseAPITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.stock = StockFactory(price=5)
        cls.user_path = reverse("user")
        cls.data = {
            "user_id": cls.user.pk,
        }

    def test_new_user_have_0_balance(self):
        res = self.post(self.user_path, status_code=200, data=self.data, format="json")
        self.assertEqual(res.data['balance'], 0)

    def test_user_with_deposits_have_more_than_zero_balance(self):
        TransactionFactory(user=self.user, amount=self.stock.price,
                           stock=None, deposit=True, withdraw=False)

        res = self.post(self.user_path, status_code=200, data=self.data, format="json")
        self.assertNotEqual(res.data['balance'], 0)

    def test_user_retreive_fails_if_no_user_exists(self):
        data = self.data.copy()
        data['user_id'] = 200
        self.post(self.user_path, status_code=404, data=data, format="json")
