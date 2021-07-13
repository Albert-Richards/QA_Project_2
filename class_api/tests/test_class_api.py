from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestClassApi(TestBase):
    def test_class(self):
        for num in range(75):
            response = self.client.get(url_for('get_class'))
            self.assertIn(response.data.decode("utf-8"),['Adept', 'Engineer', 'Soldier', 'Vanguard', 'Sentinel', 'Infiltrator'])