from unittest import TestCase
from main import argv_pars, pss


class TestArgvPars(TestCase):
    T_ARGV = {
        30: [],
        30: ["main.py"],
        1: ["main.py", "-1"],
        1: ["main.py", "-1", "0"],
        1: ["main.py", "-1", "0", "2"],
        3: ["3"],
        5: ["5", "6"],
        7: ["7.9", "7"],
    }
    def test_argv_pars(self):
        for expected, argv in self.T_ARGV.items():
            self.assertEqual(expected, argv_pars(argv))

class TestPss(TestCase):
    def test_pss(self):
        for i in range(1, 100):
            p = pss(i)
            self.assertTrue(p)
            self.assertEqual(i, len(p))