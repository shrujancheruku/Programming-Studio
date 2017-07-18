import parser
import unittest
"""
Unit tests for the parser
"""


class TestParser(unittest.TestCase):

    def test_create_data_set(self):
        """
        Checks whether returned data is accurate
        """

        data_set = parser.parse_files()
        self.assertTrue("Assignment3.0" in data_set)
        self.assertTrue("API.py" in data_set["Assignment2.1"])
        self.assertTrue("data.json" in data_set["Assignment2.1"])
        self.assertEqual(data_set["Assignment2.1"]["version"], "6898")
        self.assertEqual(data_set["Assignment2.1"]["summary"], "Pls")
        print("Passed test_create_data_set()")

    def test_revisions(self):
        """
        Checks whether the parser is returning the revisions for the file
        """

        data_set = parser.parse_files()
        self.assertTrue(len(data_set["Assignment2.1"]["API.py"]["revisions"]) > 0)
        print("Passed test_revisions()")

    def test_deleted_directory(self):
        """
        Checks whether a deleted directory shows up in the directory dict
        """

        data_set = parser.parse_files()
        self.assertTrue("Test" not in data_set)
        print("Passed test_deleted_directory()")

    def test_deleted_file(self):
        """
        Checks whether deleted files show up in a deleted directory
        """

        data_set = parser.parse_files()
        self.assertTrue("HubActors.py" not in data_set["Assignment2.1"])
        print("Passed test_deleted_file()")


if __name__ == '__main__':
    unittest.main()