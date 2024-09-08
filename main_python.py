"""
Main Python module for functionality.
"""

import pandas as pd
import matplotlib.pyplot as plt

def read_csv_file(csv):
    """
    This function returns the dataframe of the csv file we are trying to read.
    Parameters:
    1. csv: The file that is being read in
    """
    return pd.read_csv(csv)


def generalise_data(general_df, col):
    """
    This function uses the describe function to give us the statistical information.
    Parameters:
    1. general_df: The dataframe that has been created.
    2. col: The column we want descriptive statistics on.
    """
    return general_df[[col]].describe()


def histogram_visualisation(general_df, col, title, xlabel, ylabel="Frequency"):
    """
    This function is created to generate a histogram visualisation
    Parameters:
    1. general_df: The dataframe that has been created after reading in the desired csv file
    2. col: The column within the dataset for which we are creating a histogram
    3. title: Title of histogram
    4. xlabel: Label of x axis
    5. ylabel: Label of y axis
    """
    plt.figure(figsize=(10, 6))
    plt.hist(general_df[col], bins=20, edgecolor="orange")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
