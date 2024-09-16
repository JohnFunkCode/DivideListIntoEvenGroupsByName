import unittest
from assess_dataset import test_dataset_reasonability
from assess_dataset import initialize_logger


class TestAssessDataset(unittest.TestCase):

    def setup(self):
       initialize_logger()

    def test_reasonability(self):
        # Call the function
        number_of_last_names, most_common_last_name_occurrences = test_dataset_reasonability()

        # Perform assertions
        self.assertIsInstance(number_of_last_names, int, "Number of last names should be an integer")
        self.assertIsInstance(most_common_last_name_occurrences, int,
                              "Most common last name occurrences should be an integer")
        self.assertGreater(number_of_last_names, 0, "There should be at least one unique last name")
        self.assertGreater(most_common_last_name_occurrences, 0,
                           "The most common last name should have at least one occurrence")


if __name__ == '__main__':
    unittest.main()