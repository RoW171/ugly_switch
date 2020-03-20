#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Robin 'r0w' Weiland"
__date__ = "2020-03-20"
__version__ = "0.0.0"

__all__ = ()

import unittest
from ugly_switch import switch


class MyTestCase(unittest.TestCase):
    test: bool

    def setUp(self) -> None: self.test = False

    def test_no_default(self):
        s = switch[
            'a', lambda: None,
            'b', lambda: setattr(self, 'test', True)
        ]

        self.assertFalse(self.test, 'just creating the switch altered data')

        s('c')

        self.assertFalse(self.test, 'calling with a non-existing value without default altered data')

        s('a')

        self.assertFalse(self.test, 'calling a "wrong" value altered data')

        s('b')

        self.assertTrue(self.test, 'calling a "right" value did not change data')


if __name__ == '__main__':
    unittest.main()
