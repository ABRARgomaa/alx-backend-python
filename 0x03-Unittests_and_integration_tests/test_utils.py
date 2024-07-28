#!/usr/bin/env python3
"""
Parameterize a unit test
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import get_json
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    class TestAccessNestedMap
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        test function
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result,
                         f"expected to be {expected_result} but got {result}")

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        test the keyerror message
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    TestGetJson class
    """
    @patch('utils.get_json')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        test the returnvalue of get_json
        """
        mock_respons = Mock()
        mock_respons.json.return_value = test_payload
        mock_get.return_value = mock_respons
        response = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        json_data = response.json()
        self.assertEqual(json_data, test_payload, f"expected to be {test_payload} but got {json_data}")


if __name__ == '__main__':
    unittest.main()
