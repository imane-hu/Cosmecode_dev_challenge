import numpy as np
import pandas as pd

def data_info(csv_file) :
    # Read the CSV file using pandas
    data = pd.read_csv('data.csv')

    # Extract the "Score" column
    scores = data['Score']

    # Calculate the mean using pandas
    mean = scores.mean()

    # Calculate the median using pandas
    median = scores.median()

    # Calculate the standard deviation using NumPy
    std_dev = np.std(scores)

    return mean, median, std_dev
