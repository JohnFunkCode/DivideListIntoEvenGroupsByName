import sys
import unittest
import pandas as pd

import name_partitioner
from name_partitioner import NamePartionioner

class TestNamePartitioner(unittest.TestCase):
    def test_with_even_number_of_elements(self):
        np=NamePartionioner()
        np.logger.info("test_with_even_number_of_elements")

        data = {
            'first_name': ['John', 'Jane', 'Jim', 'Jack'],
            'last_name': ['Doe', 'Smith', 'Brown', 'Black']
        }
        df = pd.DataFrame(data)

        np = NamePartionioner()
        partition_boundaries = np.get_optimum_partition_boundaries(the_data=df,max_entries_per_partition=2)
        np.logger.info(partition_boundaries)
        self.assertTrue( len(partition_boundaries) > 0 )

    def test_with_odd_number_of_elements(self):
        np = NamePartionioner()
        np.logger.info("test_with_odd_number_of_elements")

        data = {
            'first_name': ['John', 'Jane', 'Jim', 'Jenny', 'Jack'],
            'last_name': ['Doe', 'Smith', 'Brown', 'Smith', 'Black']
        }


        df = pd.DataFrame(data)


        partition_boundaries = np.get_optimum_partition_boundaries(the_data=df,max_entries_per_partition=2)
        np.logger.info(partition_boundaries)
        self.assertTrue( len(partition_boundaries) > 0 )

    def test_with_spread_out_names(self):
        np = NamePartionioner()
        np.logger.info("test_with_spread_out_names")

        data = {
            'first_name': ['Jack', 'Jim', 'John', 'Jane', 'Jenny', 'John'],
            'last_name': ['Black', 'Brown', 'Doe', 'Martinez', 'Smith', 'Zawichi']
        }

        df = pd.DataFrame(data)

        partition_boundaries = np.get_optimum_partition_boundaries(the_data=df, max_entries_per_partition=2)
        np.logger.info(partition_boundaries)
        self.assertTrue(len(partition_boundaries) > 0)

    def test_twenty_split_into_three_partitions(self):
        np = NamePartionioner()
        np.logger.info("test_twenty_split_into_three_partitions")

        data = {
            'first_name': ['Jack', 'Jim', 'John', 'Jane', 'Jenny', 'John', 'Jack', 'Jim', 'John', 'Jane', 'Jenny', 'John', 'Jack', 'Jim', 'John', 'Jane', 'Jenny', 'John', 'Jack', 'Jim'],
            'last_name': ['Adams', 'Allen', 'Anderson', 'Alexander', 'Armstrong', 'Alvarez', 'Martinez', 'Miller', 'Moore', 'Martin', 'Mitchell', 'Murphy', 'Morgan', 'Morales', 'Zamora', 'Zimmerman', 'Zuniga', 'Zavala', 'Ziegler', 'Zayes']
        }

        df = pd.DataFrame(data)

        partition_boundaries = np.get_optimum_partition_boundaries(the_data=df, max_entries_per_partition=10)
        np.logger.info(partition_boundaries)
        self.assertTrue(len(partition_boundaries) > 0)

    def test_twenty_split_into_three_partitions_impossibly_low_max_entries_per_partition(self):
        np = NamePartionioner()
        np.logger.info("test_twenty_split_into_three_partitions_impossibly_low_max_entries_per_partition")
        data = {
            'first_name': ['Jack', 'Jim', 'John', 'Jane', 'Jenny', 'John', 'Jack', 'Jim', 'John', 'Jane', 'Jenny',
                           'John', 'Jack', 'Jim', 'John', 'Jane', 'Jenny', 'John', 'Jack', 'Jim'],
            'last_name': ['Adams', 'Allen', 'Anderson', 'Alexander', 'Armstrong', 'Alvarez', 'Martinez', 'Miller',
                          'Moore', 'Martin', 'Mitchell', 'Murphy', 'Morgan', 'Morales', 'Zamora', 'Zimmerman',
                          'Zuniga', 'Zavala', 'Ziegler', 'Zayes']
        }

        df = pd.DataFrame(data)

        with self.assertRaises(ValueError):
            np.get_optimum_partition_boundaries(the_data=df, max_entries_per_partition=7)

    def test_with_entire_test_data_file(self):
        np=NamePartionioner()
        np.logger.info("test_with_entire_test_data_file")
        try:
            df = pd.read_csv("random_names_with_age_diverse_1000.csv")
        except Exception as e:
            np.logger.error("Error reading the csv file: " + str(e))
            sys.exit(1)

        partition_boundaries = np.get_optimum_partition_boundaries(the_data=df, max_entries_per_partition=335)
        np.logger.info(partition_boundaries)
        self.assertTrue(len(partition_boundaries) > 0)

    def test_with_4_to_6_year_olds_in_test_data_file(self):
        np=NamePartionioner()
        np.logger.info("test_with_4_to_6_year_olds_in_test_data_file")
        try:
            df = pd.read_csv("random_names_with_age_diverse_1000.csv")
        except Exception as e:
            np.logger.error("Error reading the csv file: " + str(e))
            sys.exit(1)

        df = df.query('age >= 4 and age <= 6')

        partition_boundaries = np.get_optimum_partition_boundaries(the_data=df, max_entries_per_partition=20)
        np.logger.info(partition_boundaries)
        self.assertTrue(len(partition_boundaries) > 0)
    def test_with_7_to_8_year_olds_in_test_data_file(self): # this tests short-cut that bypassess testing 3 partitions
        np=NamePartionioner()
        np.logger.info("test_with_7_to_8_year_olds_in_test_data_file")
        try:
            df = pd.read_csv("random_names_with_age_diverse_1000.csv")
        except Exception as e:
            np.logger.error("Error reading the csv file: " + str(e))
            sys.exit(1)

        df = df.query('age >= 7 and age <= 8')

        partition_boundaries = np.get_optimum_partition_boundaries(the_data=df, max_entries_per_partition=20)
        np.logger.info(partition_boundaries)
        self.assertTrue(len(partition_boundaries) > 0)

    def test_with_9_to_11_year_olds_in_test_data_file(self):
        np=NamePartionioner()
        np.logger.info("test_with_9_to_11_year_olds_in_test_data_file")
        try:
            df = pd.read_csv("random_names_with_age_diverse_1000.csv")
        except Exception as e:
            np.logger.error("Error reading the csv file: " + str(e))
            sys.exit(1)

        df = df.query('age >= 9 and age <= 11')

        partition_boundaries = np.get_optimum_partition_boundaries(the_data=df, max_entries_per_partition=20)
        np.logger.info(partition_boundaries)
        self.assertTrue(len(partition_boundaries) > 0)

    def test_with_4_to_8_year_olds_in_test_data_file(self): # this has too many people for partitions of 20
        np=NamePartionioner()
        np.logger.info("test_with_4_to_8_year_olds_in_test_data_file")
        try:
            df = pd.read_csv("random_names_with_age_diverse_1000.csv")
        except Exception as e:
            np.logger.error("Error reading the csv file: " + str(e))
            sys.exit(1)

        df = df.query('age >= 4 and age <= 8')

        with self.assertRaises(ValueError):
            np.get_optimum_partition_boundaries(the_data=df, max_entries_per_partition=20)

    def test_with_18_to_39_year_olds_in_test_data_file(self): # this has too many people for partitions of 20
        np=NamePartionioner()
        np.logger.info("test_with_18_to_39_year_olds_in_test_data_file")
        try:
            df = pd.read_csv("random_names_with_age_diverse_1000.csv")
        except Exception as e:
            np.logger.error("Error reading the csv file: " + str(e))
            sys.exit(1)

        df = df.query('age >= 18 and age <= 39')

        with self.assertRaises(ValueError):
            np.get_optimum_partition_boundaries(the_data=df, max_entries_per_partition=20)

    def test_with_45_to_99_year_olds_in_test_data_file(self): # this has too many people for partitions of 20
        np=NamePartionioner()
        np.logger.info("test_with_45_to_99_year_olds_in_test_data_file")
        try:
            df = pd.read_csv("random_names_with_age_diverse_1000.csv")
        except Exception as e:
            np.logger.error("Error reading the csv file: " + str(e))
            sys.exit(1)

        df = df.query('age >= 45 and age <= 99')

        with self.assertRaises(ValueError):
            np.get_optimum_partition_boundaries(the_data=df, max_entries_per_partition=20)

if __name__ == '__main__':
    unittest.main()
