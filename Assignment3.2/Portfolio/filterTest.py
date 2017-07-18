import unittest
from mongoengine import *
from Portfolio import clean_comment


class TestFilter(unittest.TestCase):
    def testFruits(self):
        connect('assignment3db')
        self.assertTrue(clean_comment('fuck') == 'flower')
        self.assertTrue(clean_comment('bitch') == 'my dear lady')
        self.assertTrue(clean_comment('dick') == 'richard')
        self.assertFalse(clean_comment('asshole') == 'asshole')

if __name__ == '__main__':
    unittest.main()