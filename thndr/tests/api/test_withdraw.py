from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from thndr.factories.user_factory import UserFactory
from thndr.tests.base_api_test_case import BaseAPITestCase


class WithdrawTestCase(APITestCase, BaseAPITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.withdraw_path = reverse("account-withdraw")
        cls.depost_path = reverse("account-deposit")

    def test_withdraw_only_deposit_to_real_users(self):
        data = {}
        data['user_id'] = "wrong stuff"
        data['amount'] = "wrong stuff"
        self.post(self.withdraw_path, status_code=400, data=data, format="json")

    def test_withdraw_fails_with_wrong_body(self):
        data = {}
        data['wrong'] = "wrong stuff"
        self.post(self.withdraw_path, status_code=400, data=data, format="json")

    def test_withdraw_fails_if_amount_is_not_an_int(self):
        data = {}
        data['user_id'] = self.user.pk
        data['amount'] = "wrong"
        self.post(self.withdraw_path, status_code=400, data=data, format="json")

    def test_withdraw_to_a_user_with_no_balance_fails(self):
        data = {}
        data['user_id'] = self.user.pk
        data['amount'] = 5
        self.post(self.withdraw_path, status_code=400, data=data, format="json")

    def test_withdraw_to_a_user_with_balance(self):
        data = {}
        data['user_id'] = self.user.pk
        data['amount'] = 5
        self.post(self.depost_path, status_code=200, data=data, format="json")

        self.post(self.withdraw_path, status_code=200, data=data, format="json")
