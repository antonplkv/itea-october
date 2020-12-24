import unittest
from source_code import number_randomize


class TestMySourceCode(unittest.TestCase):

    def setUp(self) -> None:
        self.quantity = 10

    def test_number_randomize(self):

        self.assertEqual(len(
            list(number_randomize(2))),
            2)

        for i in number_randomize(self.quantity):
            self.assertIsInstance(i, int)

        with self.assertRaises(TypeError):
            list(number_randomize('eqw'))