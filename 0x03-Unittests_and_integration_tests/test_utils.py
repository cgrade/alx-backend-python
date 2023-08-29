#!/usr/bin/env python3
""" A unit test module that runs test on
    `utils.access_nested_map` method.
"""

from utils import access_nested_map
import unittest
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
