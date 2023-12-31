#!/usr/bin/env python3
""" A unit test module that runs test on
    `utils.access_nested_map` method.
"""

from utils import access_nested_map, get_json, memoize
import unittest
from unittest.mock import patch, Mock
from unittest.mock import patch
from parameterized import parameterized, parameterized_class
from typing import (
    Mapping,
    Sequence,
    Any
)


class TestAccessNestedMap(unittest.TestCase):
    """ A class that inherit from `TestCase`
        to test for Access Nested Map method
        in utils.py
    """

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    @parameterized.expand([
            ({"a": 1}, ["a"], 1),
            ({"a": {"b": 2}}, ["a"], {'b': 2}),
            ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected_result: Any):
        """ A test method that test for correcteness,
            with `assertEqual()` of TestCase Class.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
            ({}, ["a"], 'KeyError: a'),
            ({"a": 1}, ["a", "b"], 'KeyError: b'),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence, expected_result: Any):
        """ A test method that test for Exception with
            `assertRaises()` method of TestCase class.
        """
        with self.assertRaises(KeyError, msg=expected_result):
            result = access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ A class that inherit from `TestCase`
        to test `get_json()` method of
        `utils.py`
        in utils.py
    """

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def test_get_json(self, url: str):
        """ A test method that tests for correctness of the
            `get_json()` method of utils.py
        """
    @parameterized.expand(
        [
            ('http://example.com', {'payload': True}),
            ('http://holberton.io', {'payload': False})
        ]
    )
    def test_get_json(self, url, expected_output):
        """_summary_
        """
        mock_response = Mock()
        mock_response.json.return_value = expected_output
        with patch('requests.get', return_value=mock_response):
            response = get_json(url)

            self.assertEqual(response, expected_output)


class TestMemoize(unittest.TestCase):
    """_summary_

    Args:
                    unittest (_type_): _description_
    """

    def test_memoize(self):
        """_summary_

        Returns:
                _type_: _description_
        """

        class TestClass:
            """_summary_
            """

            def a_method(self):
                """_summary_

                Returns:
                        _type_: _description_
                """
                return 42

            @memoize
            def a_property(self):
                """_summary_

                Returns:
                        _type_: _description_
                """
                return self.a_method()

        test_obj = TestClass()

        with patch.object(test_obj, 'a_method') as mock_method:
            mock_method.return_value = 42

            result1 = test_obj.a_property
            result2 = test_obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
