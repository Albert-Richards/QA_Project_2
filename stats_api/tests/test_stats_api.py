
from flask import url_for, jsonify
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestStatsApi(TestBase):
    def test_stats(self):
        species = ['Krogan', 'Quarian', 'Batarian', 'Drell']
        classes = ['Nemesis', 'Bastion', 'Commando', 'Shock Trooper', 'Operative', 'Medic']
        for i in range(len(species)):
            for j in range(len(classes)):
                response = self.client.post(url_for('get_stats'), json= {"species":species[i], "class":classes[j]})
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json["Combat"] + response.json["Biotic"] + response.json["Tech"], 23)