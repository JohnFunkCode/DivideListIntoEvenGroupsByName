import logging
import os
import sys
from datetime import datetime
import math
import pandas as pd

class NamePartionioner:
    ''' class to manage split a list of competitor's into even groups based on last name'''

    @property
    def _constructor(self):
        return NamePartioner

    def __init__(self):
        '''setup instance variables'''
        super().__init__()

    def get_partition_boundaries(self, the_data:pd.DataFrame, max_entries_per_partition:int) -> list:
        print(the_data)

        # calculate the number of partitions
        number_of_partitions = math.ceil((len(the_data) / max_entries_per_partition))
        print(f'number_of_partitions:', number_of_partitions)

        return [{'A','F'},{'G','L'},{'M','R'}]



if __name__ == '__main__':
    data = {
        'first_name': ['John', 'Jane', 'Jim', 'Jenny', 'Jack'],
        'last_name': ['Doe', 'Smith', 'Brown', 'Smith', 'Black']
    }
    df = pd.DataFrame(data)

    # Add a column to the dataframe with the first letter of the 'Last Name' field
    df['LastNameFirstLetter'] = df['last_name'].str[0]

    goal = 2

    i=0
    for boundry1 in range(1,26):
        # print(f'A-{chr(64+boundry1)}')
        for boundry2 in range(boundry1+1,26):
            # print(f'A-{chr(64 + boundry1)}, {chr(64 + boundry1 + 1)}-{chr(64 + boundry2)}, {chr(64 + boundry2+1)}-Z')
            query_string1=f'LastNameFirstLetter >= "A" and LastNameFirstLetter <= "{chr(64 + boundry1)}"'
            bucket1 = df.query(query_string1)
            sizeofbucket1 = len(bucket1)

            query_string2=f'LastNameFirstLetter >= "{chr(64 + boundry1 + 1)}" and LastNameFirstLetter <= "{chr(64 + boundry2)}"'
            bucket2 = df.query(query_string2)
            sizeofbucket2 = len(bucket2)

            query_string3=f'LastNameFirstLetter >= "{chr(64 + boundry2 + 1)}" and LastNameFirstLetter <= "Z"'
            bucket3 = df.query(query_string3)
            sizeofbucket3 = len(bucket3)

            score = (goal-sizeofbucket1)**2 + (goal-sizeofbucket2)**2 + (goal-sizeofbucket3)**2

            if(score==1):
             print(f'A-{chr(64 + boundry1)}:{sizeofbucket1}, {chr(64 + boundry1 + 1)}-{chr(64 + boundry2)}:{sizeofbucket2}, {chr(64 + boundry2+1)}-Z:{sizeofbucket3} - score={score}')

            i=i+1
    print(i)

