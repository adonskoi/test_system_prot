import os, unittest


from case.second import SecondCase


class SecondTest(unittest.TestCase):
    def test_run(self):
        case = SecondCase(2, "second")
        self.assertEqual(case.run(), 1024)

    def test_prep(self):
        case = SecondCase(2, "second")
        self.assertEqual(case.prep(2), "ok")

    def test_prep_raises(self):
        case = SecondCase(2, "second")
        with self.assertRaises(Exception) as e:
            case.prep(0.5)
        self.assertEqual(str(e.exception), "Memory size less then 1 GB")

    def test_execute(self):
        case = SecondCase(4, "erg")
        self.assertEqual(case.execute(), True)

    def test_clean_up(self):
        case = SecondCase(2, "second")
        case.run()
        self.assertEqual(case.clean_up(), "ok")
        self.assertEqual(case.clean_up(), "ok")

