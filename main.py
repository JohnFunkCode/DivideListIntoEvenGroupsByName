import logging
import os
import sys
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

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

    # read the csv file
    logging.info("Reading the csv file")
    try:
        df = pd.read_csv("random_names_with_age_diverse_100.csv")
    except Exception as e:
        logging.error("Error reading the csv file: " + str(e))
        sys.exit(1)

    logger.info("Creating a bar chart of the distribution of the first letters of the last names")
    # Extract the first letter of the 'Last Name' field
    df['LastNameFirstLetter'] = df['Last Name'].str[0]

    # Sort the counts by the first letter of the last name
    first_letter_counts = df['LastNameFirstLetter'].value_counts().sort_index()

    # Create bar chart
    plt.bar(first_letter_counts.index, first_letter_counts.values, color='skyblue')
    plt.xlabel('First Letter of Last Name')
    plt.ylabel('Count')
    plt.title('Distribution of First Letters of Last Names')
    plt.show()

    # # Create pie chart
    # plt.pie(first_letter_counts.values, labels=first_letter_counts.index, autopct='%1.1f%%', colors=plt.cm.Paired.colors)
    # plt.title('Distribution of First Letters of Last Names')
    # plt.show()