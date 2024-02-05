#!/usr/bin/env python3
"""Test suites for tasks 0-3"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Union
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """Contains test suite for Access Nested Map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nmap: Mapping, npath: Sequence,
                               nresult: Union[Mapping, int]) -> None:
        """A method to test the return value of the function"""
        self.assertEqual(access_nested_map(nmap, npath), nresult)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nmap: Mapping, npath: Sequence,
                                         nresult: KeyError):
        """A method to test exception thrown by a function"""
        with self.assertRaises(nresult):
            access_nested_map(nmap, npath)


class TestGetJson(unittest.TestCase):
    """Contains test suite for Get Json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, req, res, mock_requests_get):
        """A method that mocks a requests json response"""
        mock_requests_get.return_value.json.return_value = res
        self.assertEqual(get_json(req), res)
        mock_requests_get.assert_called_once_with(req)


class TestMemoize(unittest.TestCase):
    """Contains test suite for memoized method"""
    def test_memoize(self):
        """A method to test the actual memoization"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock_method.assert_called_once()
