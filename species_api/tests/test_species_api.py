from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestSpeciesApi(TestBase):
    def test_species(self):
        for num in range(15):
            response = self.client.get(url_for('get_species'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(response.data.decode("utf-8"), ['Krogan', 'Quarian', 'Batarian', 'Drell'])