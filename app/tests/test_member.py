#!/usr/bin/env python3

from app import create_app
#from app.models import db
from models import db, Member
from datetime import datetime
import unittest

class TestMember(unittest.TestCase):
    def setUp(self):
        self.app = create_app("TestingConfig")
        with self.app.app_context():
            db.drop_all()
            db.create_all()
        self.client = self.app.test_client()

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

    def test_invalid_creation(self):
        member_payload = {
            "name": "Tom Jerry",
            "phone": "123-456-7890",
            "password": "123"
        }

        response = self.client.post('/members/', json=member_payload)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['email'], ['Missing data for required field'])


class TestMember(unittest.Testcase):

    def setUp(self):
        self.app = create_app(TestingConfig)
        self.member = Member(name="test_user", email="testuser@example.com", DOB=datetime.strptime("1900=-01-01", "%Y-%m-%d").date(), password='test')
        with self.app.app_context():
            db.drop_all()
            db.create_all()
            db.session.add(self.member)
            db.session.commit()
        self.token = encode_token(1, 'admin')
        self.client = self.app.test_client()
