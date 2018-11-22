import unittest
import json
from app.api.tests.test_base import BaseTest


class TestUser(BaseTest):
    """Tests the User model"""

    def test_new_user(self):
        respo = self.client.post(
            'api/v2/auth/signup', data=json.dumps(self.sample_user), content_type='application/json')
        result = json.loads(respo.data.decode())
        print("\n", result, "\n")
        self.assertEqual(respo.status_code, 201)
        self.assertEqual(result["message"], "User registration successful")
        self.assertEqual(self.sample_user['username'], result[
                         'data']['username'])

    def test_login_user(self):
        respo = self.client.post(
            'api/v2/auth/login', data=json.dumps(self.sample_login), content_type='application/json')
        result = json.loads(respo.data.decode())
        self.assertEqual(respo.status_code, 201)
        self.assertEqual(result["message"], "User login successful")


if __name__ == "__main__":
    unittest.main()
