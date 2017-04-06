# -*- coding: utf-8 -*-

from .context import configparserdb

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(configparserdb_read.("test.cfg", "one", "testelem"))


if __name__ == '__main__':
    unittest.main()
