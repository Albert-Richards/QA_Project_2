from flask import url_for
from flask_testing import TestCase
import requests_mock

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as m:
            m.get('http://species_api:5000/get_species', text='Geth')
            m.get('http://class_api:5000/get_class', text='Intruder')
            m.post('http://stats_api:5000/get_stats', json = {"Combat":7, "Biotic":0, "Tech":12})
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Species: Geth', response.data)
            self.assertIn(b'Class: Intruder', response.data)
            self.assertIn(b'Combat: 7', response.data)
            self.assertIn(b'Biotic: 0', response.data)
            self.assertIn(b'Tech: 12', response.data)