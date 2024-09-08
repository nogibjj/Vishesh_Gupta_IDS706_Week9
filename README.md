# Vishesh_Gupta_IDS706_Week2
## Assignment 2 for Data Engineering

[![CI](https://github.com/nogibjj/Vishesh_Gupta_IDS706_Week2/actions/workflows/CI.yml/badge.svg)](https://github.com/nogibjj/Vishesh_Gupta_IDS706_Week2/actions/workflows/CI.yml)

## Purpose:
The purpose of this project is to build on the the previous project (making a python template i.e. Scaffolding) and generate descriptive statistics on datasets using Pandas.

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

## Check test errors
Test code `make test`

<img width="968" alt="Screenshot 2024-09-08 at 9 44 26 AM" src="https://github.com/user-attachments/assets/f8118a7c-87a4-4a7f-882f-96cace098ef6">

## Summary stats showing the results for inputed dataset:

<img width="837" alt="Screenshot 2024-09-08 at 9 45 09 AM" src="https://github.com/user-attachments/assets/7b55e37d-36a2-48f9-b1e6-3d01b004c3ec">

## Data Visualisation 

<img width="902" alt="Screenshot 2024-09-08 at 9 44 14 AM" src="https://github.com/user-attachments/assets/56f67d1c-bc80-4851-afce-534b278a6628">

