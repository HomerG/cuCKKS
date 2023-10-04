import os
import sys
import time
import unittest

from src.params import CKKSParameters

TEST_DIRECTORY = os.path.dirname(__file__)

class TestParams(unittest.TestCase):
    def setUp(self):
        self.degree = int(4096)
        self.ciph_modulus = 1 << 600
        self.big_modulus = 1 << 1200
        self.scaling_factor = 1 << 30

        self.params = CKKSParameters(poly_degree=self.degree,
                                     ciph_modulus=self.ciph_modulus,
                                     big_modulus=self.big_modulus,
                                     scaling_factor=self.scaling_factor)

        print("hello1")

    def test(self):
        self.params.print_parameters()


if __name__ == '__main__':
    res = unittest.main(verbosity=3, exit=False)
