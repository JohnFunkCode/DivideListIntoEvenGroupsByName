import unittest
import pandas as pd
from name_partitioner import NamePartionioner

class TestNamePartitioner(unittest.TestCase):
    def test_partition_boundaries_with_even_number_of_elements(self):
        data = {
            'first_name': ['John', 'Jane', 'Jim', 'Jack'],
            'last_name': ['Doe', 'Smith', 'Brown', 'Black']
        }
        df = pd.DataFrame(data)

        np = NamePartionioner()
        partition_boundaries = np.get_partition_boundaries(the_data=df,max_entries_per_partition=2)
        print(partition_boundaries)
        self.assertTrue( len(partition_boundaries) > 0 )

    def test_partition_boundaries_with_odd_number_of_elements(self):
        data = {
            'first_name': ['John', 'Jane', 'Jim', 'Jenny', 'Jack'],
            'last_name': ['Doe', 'Smith', 'Brown', 'Smith', 'Black']
        }
        df = pd.DataFrame(data)

        np = NamePartionioner()
        partition_boundaries = np.get_partition_boundaries(the_data=df,max_entries_per_partition=2)
        print(partition_boundaries)
        self.assertTrue( len(partition_boundaries) > 0 )

if __name__ == '__main__':
    unittest.main()