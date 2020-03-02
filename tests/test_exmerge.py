# -*- coding: utf-8 -*-

import unittest

import os
import sys

script_dir = os.path.dirname(__file__)
import_dir = os.path.join(script_dir, "..")
sys.path.insert(0, import_dir)

import pandas as pd
from lib.iodata.iodata import load_data, save_data
from exmerge import exmerge


class LoadTest(unittest.TestCase):
    def testSums(self):
        df1 = load_data("tests/fixtures/test_data.xlsx")
        df2 = load_data("tests/fixtures/test_voc.xlsx")

        result = exmerge(df1, df2)

        df1_sum = int(
            df1[df1.select_dtypes(["int", "float"]).columns.tolist()].sum().sum()
        )
        result_sum = int(
            result[result.select_dtypes(["int", "float"]).columns.tolist()].sum().sum()
        )

        self.assertEqual(
            df1_sum,
            result_sum,
            msg=f"Initial sum is {df1_sum}, sum after merge is {result_sum}. Should be equal",
        )


if __name__ == "__main__":
    unittest.main()
