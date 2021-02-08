from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from thndr.factories.user_factory import UserFactory
from thndr.tests.base_api_test_case import BaseAPITestCase


class DepositTestCase(APITestCase, BaseAPITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.deposit_path = reverse("account-deposit")

    def test_deposits_to_an_existing_user(self):
        data = {}
        data['user_id'] = self.user.pk
        data['amount'] = 5
        self.post(self.deposit_path, status_code=200, data=data, format="json")

    def test_deposits_only_deposit_to_real_users(self):
        data = {}
        data['user_id'] = "wrong stuff"
        data['amount'] = "wrong stuff"
        self.post(self.deposit_path, status_code=400, data=data, format="json")

    def test_deposits_fails_with_wrong_body(self):
        data = {}
        data['wrong'] = "wrong stuff"
        self.post(self.deposit_path, status_code=400, data=data, format="json")

    def test_deposits_fails_if_amount_is_not_an_int(self):
        data = {}
        data['user_id'] = self.user.pk
        data['amount'] = "wrong"
        self.post(self.deposit_path, status_code=400, data=data, format="json")
