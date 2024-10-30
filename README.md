# Vishesh_Gupta_IDS706_Week9
## Assignment 9 for Data Engineering

[![CI](https://github.com/nogibjj/Vishesh_Gupta_IDS706_Week9/actions/workflows/CI.yml/badge.svg)](https://github.com/nogibjj/Vishesh_Gupta_IDS706_Week9/actions/workflows/CI.yml)

## Purpose:
# Project: Cloud-Hosted Jupyter Notebook with Google Colab and GitHub Integration

This project involves setting up a cloud-hosted Jupyter Notebook on Google Colab, performing data manipulation on a sample dataset, and connecting the notebook to GitHub for version control and sharing.

## Requirements

1. **Google Colab**: Access to Google Colab to create and run Jupyter Notebooks online.
2. **GitHub Account**: A GitHub account to store, share, and manage the project files.
3. **Sample Dataset**: A dataset to perform data manipulation tasks.
4. **Basic Python Libraries**: Pandas and Numpy for data manipulation.

## Setup and Instructions

### 1. Setting up Google Colab

Google Colab is a cloud-hosted platform that allows you to run Jupyter Notebooks without any local setup. Here’s how to set it up:

- Go to [Google Colab](https://colab.research.google.com/).
- Sign in with your Google account.
- Start a new notebook by clicking **New Notebook** or open an existing one.

### 2. Performing Data Manipulation Tasks

To perform data manipulation, load your sample dataset and install necessary libraries. Here’s an example:

### 3. Connecting Google Colab to GitHub

1. **Save Notebook to GitHub**:
   - Open your notebook in Google Colab.
   - Go to **File** > **Save a copy in GitHub...**
   - Select your repository, add a description, and save.
   
2. **Use Google Colab to Push Changes**:
   - After making changes, you can save the notebook directly to GitHub as described above.

### 4. Following the Video Tutorial

You can refer to [this video tutorial](https://youtu.be/6Egd-OMLLV4?si=1yDZW4WBE1pIwSMB) for step-by-step guidance on setting up Google Colab and connecting it to GitHub.

### Analysis information 
Here you can find:
- .github contains the .yml file 
- Makefile to automate the python task
- main_python.py contains the main function which is the multiplication between two numbers
- test_main.py contains the testing function for main_python.py by having three assertions to ensure our code is executing as expeceted
- Requirements.txt specify the library requirements to run the code
- .devcointainer has a .json file and a Dockerfile

Within the main_python.py file you see:
1. read_csv: This function returns the dataframe of the csv file we are trying to read. We use encoding="ISO-8859-1", delimiter=";" to ensure we import the data set correctly and have it clean for analysing.
2. generalise_data: This function uses the describe function to give us the statistical information. The describe function used doesn't provide us with a median therefore we have appended the median value to our final result. We pass in the dataframe and column on which we would like to obtain all the statistical information. 
3. line_graph_visualisation: This function generates a line graph to visualize the relationship between two variables from a DataFrame.
4. bar_graph_visualisation: This function generates a bar graph for data visualisation purposes.

## Check test errors
Test code `make test`

<img width="968" alt="Screenshot 2024-09-08 at 9 44 26 AM" src="https://github.com/user-attachments/assets/f8118a7c-87a4-4a7f-882f-96cace098ef6">

## Summary stats showing the results for inputed dataset:

<img width="837" alt="Screenshot 2024-09-08 at 9 45 09 AM" src="https://github.com/user-attachments/assets/7b55e37d-36a2-48f9-b1e6-3d01b004c3ec">

## Data Visualisation 

<img width="902" alt="Screenshot 2024-09-08 at 9 44 14 AM" src="https://github.com/user-attachments/assets/56f67d1c-bc80-4851-afce-534b278a6628">

<img width="962" alt="Screenshot 2024-09-08 at 2 51 41 PM" src="https://github.com/user-attachments/assets/2bd9d88f-933d-4e4a-90f4-51e3aa270c3a">



