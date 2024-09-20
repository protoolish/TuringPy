import unittest

from turingpy.symbol import Symbol, BlankType

class TestSymbol(unittest.TestCase):
    def test_init(self):

        s = Symbol("s")
        with self.assertRaises(ValueError):
            s = Symbol("symbol")

        with self.assertRaises(ValueError):
            b = Symbol(None) # type: ignore

        with self.assertRaises(ValueError):
            c = Symbol(1) # type: ignore

    def test_create(self):

        s = Symbol.create("s")
        self.assertEqual(s, Symbol("s"))

        b = Symbol.create(None)
        self.assertEqual(b, BlankType())

        with self.assertRaises(ValueError):
            c = Symbol.create([])

        with self.assertRaises(ValueError):
            d = Symbol.create("longer string")

    def test_eq(self):
        self.assertEqual(Symbol("a"), "a")
        self.assertEqual(Symbol("a"), Symbol("a"))
        self.assertEqual(Symbol("a"), Symbol.create("a"))

        self.assertEqual(Symbol.create(None), BlankType())
        self.assertEqual(BlankType(), BlankType())
        self.assertIs(Symbol.create(None), BlankType())
        self.assertIs(BlankType(), BlankType())
        self.assertNotEqual(BlankType(), Symbol(" "))

    def test_str(self):
        self.assertEqual(str(Symbol("a")), "a")
        self.assertEqual(str(Symbol.create("b")), "b")

        self.assertEqual(str(BlankType()), " ")
        self.assertNotEqual(BlankType(), " ")

    def test_types(self):
        symbol = Symbol("a")
        blank = BlankType()
        self.assertTrue(isinstance(symbol, Symbol))
        self.assertTrue(isinstance(blank, Symbol))

        self.assertTrue(isinstance(blank, BlankType))
        self.assertFalse(isinstance(symbol, BlankType))