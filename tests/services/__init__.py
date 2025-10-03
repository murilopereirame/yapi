import os
import unittest

if __name__ == '__main__':
    test_dir = os.path.dirname(__file__)
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=test_dir, pattern="*_test.py")

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)