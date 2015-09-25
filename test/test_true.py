#!/usr/bin/env python3
"""Tests for true.py"""

import unittest

import true

class TestTrue(unittest.TestCase):

    def test_exit(self):
        with self.assertRaises(SystemExit) as context:
            true.main()

        self.assertEqual(context.exception.code, 0)

if __name__ == '__main__':
    unittest.main()
