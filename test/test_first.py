import os, unittest
from pathlib import Path


from case.first import FirstCase


class FirstTest(unittest.TestCase):
    def test_prep(self):
        case = FirstCase(1, "first", time=1572003634)
        self.assertEqual(case.prep(), "ok")

    def test_prep_raises(self):
        case = FirstCase(1, "first", time=157200363)
        with self.assertRaises(Exception) as e:
            case.prep()
        self.assertEqual(str(e.exception), "unix time  % 2 != 0")

    def test_run(self):
        case = FirstCase(1, "first")
        self.assertEqual(case.run(), os.listdir(Path.home()))

    def test_execute(self):
        case = FirstCase(1, "first", time=1572003634)
        self.assertEqual(case.execute(), True)

    def test_execute_stop_and_false_on_prep(self):
        case = FirstCase(1, "first", time=157200363)
        self.assertEqual(case.execute(), False)
