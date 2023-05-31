# import unittest to use its   functionality.
import sys
import unittest


# Create new test case to implement and group tests.
class TestCaseClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # is executed once cest case starts.
        print('Test Case "TestCaseClass" has started.')

    @classmethod
    def tearDownClass(cls):
        # is executed once Test Case finishes.
        print('Test Case "TestCaseClass" has finished.')

    def setUp(self):
        # is executed before every test in Test Case.
        print('Check {} has started.'.format(self._testMethodName))

    def tearDown(self):
        # is executed after every test in Test Case.
        print('Check {} has finished.'.format(self._testMethodName))

    def test_1(self):
        # test checks if "1" is in the target list.
        self.assertIn(1, [2, 1, 4])

    def test_2(self):
        # test checks if "a" and "b" are referring to the same
        # object.
        a = b = 1
        self.assertIs(a, b)

    def test_3(self):
        # test checks if "a" and "b" values are equal.
        a = [1, 2, 3]
        b = [1, 2, 3]
        self.assertEqual(a, b)


# create new Test Suite
# suite_1 = unittest.TestSuite()
# convert Test Case to Test Suite
# add to existing Test Suite
# suite_1.addTest(unittest.TestLoader.loadTestsFromTestCase(estCaseClass))

# or
# create new Test Suite
# suite_2 = unittest.TestSuite()
# instantiate Test Case object and add to existing Test Suite
# suite_2.addTest(TestCaseClass())


class MyTestCase(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        # Test should not be executed in any case
        # self.fail() - method that fails
        # test with text in brackets
        self.fail("shouldn't happen")

    @unittest.skipUnless(sys.platform.startswith("win"),
                         "requires Windows")
    def test_windows_support(self):
        # Test should be skipped if OS is not Windows
        pass


@unittest.skip("Whole TestCase class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass


class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")
