#!/usr/bin/python3
"""
Unit tests for AirBnB clone API's app.py
"""

import os
import unittest
from unittest.mock import patch
from flask import Flask, jsonify
from models import storage
from api.v1.app import app, close_storage, not_found, main


class TestApp(unittest.TestCase):
    def test_teardown_appcontext(self):
        with app.app_context():
            self.assertIsNone(close_storage(None))

    def test_errorhandler_404(self):
        with app.test_request_context('/nonexistent'):
            response = not_found(None)
            self.assertIsInstance(response, tuple)  # Ensure response is a tuple
            self.assertEqual(response[1], 404)  # Check the status code in the tuple
            self.assertEqual(response[0].get_json(), {"error": "Not found"})  # Check JSON content


    def test_main(self):
        with patch.object(app, 'run', return_value=None):
            with patch('api.v1.app.os.getenv', side_effect=['0.0.0.0', '5000']):
                self.assertIsNone(main())

if __name__ == "__main__":
    unittest.main()
