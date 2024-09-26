import logging
import os
import sys
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def initialize_logger():
    # setup logging to file and to stdout
    if(not os.path.exists("logs")):
        os.makedirs("logs")
    errorLogFileName = "logs/error_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".log"
    logger = logging.getLogger('')
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(errorLogFileName)
    sh = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s %(message)s', datefmt='%H:%M:%S')
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(sh)
    return logger

def test_dataset_reasonability() -> tuple[int, int]:
    logger = logging.getLogger()
    logging.info("Reading the csv file")
    try:
        df = pd.read_csv("random_names_with_age_diverse_1000.csv")
    except Exception as e:
        logging.error("Error reading the csv file: " + str(e))
        sys.exit(1)


    # Create a new dataframe with the last names grouped by 'Last Name' and count occurrences
    last_name_counts = df.query('`Last Name` == `Last Name`').groupby('Last Name').size().reset_index(name='Count')
    number_of_last_names = len(last_name_counts)

    # # Display the result
    # with pd.option_context('display.max_rows', None,
    #                        'display.max_columns', None,
    #                        'display.precision', 3,
    #                        ):
    #     logger.info(last_name_counts)

    logger.info(f'The dataset contains {number_of_last_names} unique last names.')

    # Find the last name with the most occurrences
    most_common_last_name = last_name_counts.loc[last_name_counts['Count'].idxmax()]
    most_common_last_name_occurrences = int(most_common_last_name["Count"])
    # logging.info the result
    logger.info(
        f'The most common last name is "{most_common_last_name["Last Name"]}" with {most_common_last_name_occurrences} occurrences.')
    #
    # #Create bar chart with the distribution of the first letters of the last names
    #
    # #Add a column to the dataframe with the first letter of the 'Last Name' field
    # df['LastNameFirstLetter'] = df['Last Name'].str[0]
    #
    # # Sort the counts by the first letter of the last name
    # first_letter_counts = df['LastNameFirstLetter'].value_counts().sort_index()
    #
    # plt.bar(first_letter_counts.index, first_letter_counts.values, color='skyblue')
    # plt.xlabel('First Letter of Last Name')
    # plt.ylabel('Count')
    # plt.title('Distribution of First Letters of Last Names')
    # plt.show()

    # # Create pie chart
    # plt.pie(first_letter_counts.values, labels=first_letter_counts.index, autopct='%1.1f%%', colors=plt.cm.Paired.colors)
    # plt.title('Distribution of First Letters of Last Names')
    # plt.show()
    # Test the reasonability of the dataset
    return number_of_last_names, most_common_last_name_occurrences


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    initialize_logger()
    test_dataset_reasonability()

