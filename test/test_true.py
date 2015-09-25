#!/usr/bin/env python3
"""Tests for true.py"""

import unittest

class TestTrue(unittest.TestCase):

    def test_exit(self):
        with self.assertRaises(SystemExit) as context:
            import true

        self.assertEqual(context.exception.code, 0)
        self.assertEqual(context.exception.message, 0)

if __name__ == '__main__':
    unittest.main()
