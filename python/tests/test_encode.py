import os
import sys
import time
import unittest

from src.params import CKKSParameters
from src.encode import CKKSEncoder
from tests.helper import check_complex_vector_approx_eq
from util.random_sample import sample_random_complex_vector
from util.plaintext import Plaintext

TEST_DIRECTORY = os.path.dirname(__file__)

class TestEncoder(unittest.TestCase):


    def setUp(self):
        self.degree = int(4)
        self.ciph_modulus = 1 << 40
        self.big_modulus = 1 << 1200
        self.scaling_factor = 1 << 6

        params = CKKSParameters(poly_degree=self.degree,
                                ciph_modulus=self.ciph_modulus,
                                big_modulus=self.big_modulus,
                                scaling_factor=self.scaling_factor)
        self.encoder = CKKSEncoder(params)

    def run_test_encode_decode(self, vec):
        plain = self.encoder.encode(vec, self.scaling_factor)
        value = self.encoder.decode(plain)
        check_complex_vector_approx_eq(vec, value, error=0.1)

    def test_encode_decode_01(self):
        vec = sample_random_complex_vector(self.degree // 2)
        vec = [complex(3, 4), complex(2, -1)]
        print("VEC: \n")
        print(vec)
        self.run_test_encode_decode(vec)

if __name__ == '__main__':
    res = unittest.main(verbosity=3, exit=False)