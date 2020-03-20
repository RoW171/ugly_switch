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
