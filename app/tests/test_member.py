#!/usr/bin/env python3

from app import create_app
from app.models import db
import unittest

class TestMember(unittest.TestCase):
    def setUp(self):
        self.app = create_app("TestingConfig")
        with self.app_context():
            db.drop_all()
            db.create_all()
        self.client = self.app.test_cllient()

    def test_create_member(self):
        member_payload = {
            "name": "Tom Jerry",
            "email": "tomj@example.com",
            "DOB": "1900-01-01",
            "password": "123"
        }

        response = self.client.post('/members/', json=member_payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], "Tom Jerry")
