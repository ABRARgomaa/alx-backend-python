#!/usr/bin/env python3
"""
Parameterize a unit test
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import (access_nested_map, get_json)


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
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test for the utils.get_json function to check
        that it returns the expected result."""
        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()


if __name__ == '__main__':
    unittest.main()
