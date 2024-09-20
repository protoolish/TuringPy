import unittest
from turingpy.tape import Tape

class TestTape(unittest.TestCase):
    def test_init(self):
        tape = Tape()
        self.assertEqual(tape.read(), Tape.BLANK)

        tape_string = "abc"
        tape = Tape(tape_string)
        self.assertEqual(tape.reads(), "a")
        self.assertEqual(tape.reads(), "b")
        self.assertEqual(tape.reads(), "c")
        self.assertEqual(tape.reads(), Tape.BLANK)

    def test_read_write(self):

        tape = Tape()

        self.assertEqual(tape.read(), Tape.BLANK)
        tape.write("x")
        self.assertEqual(tape.read(), "x")

    def test_reads_writes(self):
        tape = Tape()
        test_string = "abcdefghijklmnpoqrstuvwxyz"
        for c in test_string:
            tape.writes(c, reverse=True)

        tape.step()

        for c in reversed(test_string):
            self.assertEqual(tape.reads(), c)

    def test_step(self):
        tape = Tape("0123456789")
        self.assertEqual(tape.read(), "0")

        for _ in range(9): tape.step()

        self.assertEqual(tape.read(), "9")

        tape.step()

        self.assertEqual(tape.read(), Tape.BLANK)

    def test_step_reverse(self):
        tape = Tape("0123456789")

        self.assertEqual(tape.read(), "0")

        for _ in range(9): tape.step()

        self.assertEqual(tape.read(), "9")

        tape.step(reverse=True)
        self.assertEqual(tape.read(), "8")

    def test_scan(self):
        tape = Tape("0123456789")

        scanner = tape.scan()
        values = []

        for _ in range(11):
            values.append(next(scanner))

        test_vals = [str(i) for i in range(10)]
        test_vals.append(Tape.BLANK)

        self.assertEqual(values, test_vals)

    def test_copy(self):
        tape = Tape("abc")

        tape.step()
        tape.write("x")
        tape_copy = tape.copy()

        self.assertEqual(tape.read(), "x")
        self.assertEqual(tape_copy.read(), "x")

        tape.step()
        tape_copy.write("y")

        self.assertEqual(tape.read(), "c")
        self.assertEqual(tape_copy.read(), "y")

        self.assertNotEqual(tape, tape_copy)

    def test_reset(self):
        tape = Tape("abc")
        tape.step()
        tape.step()
        self.assertEqual(tape.read(), "c")
        tape.reset()
        self.assertEqual(tape.read(), "a")
        tape.step(reverse=True)
        tape.step(reverse=True)
        tape.reset()
        self.assertEqual(tape.read(), "a")

