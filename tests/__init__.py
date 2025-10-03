import os
import unittest

def run_all_tests():
    test_dir = os.path.dirname(__file__)

    suite = unittest.defaultTestLoader.discover(
        start_dir=test_dir,
        pattern="*_test.py",
        top_level_dir=os.path.dirname(__file__)
    )

    runner = unittest.TextTestRunner(verbosity=2, failfast=True)
    runner.run(suite)

if __name__ == "__main__":
    run_all_tests()