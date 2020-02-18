# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The average of the changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period

#import csv

import os
import csv

budget_df=os.path.join("..", "PyBank", "budget_data.csv")
budget_df

# create obejects from CSV file
total_months = 0
# empty lists for iteration across rows for month variable 
total_months = [] 
# read csv 
with open("budget_data.csv", newline = '') as file:
    reader = csv.reader(file, delimiter =",")
    for row in reader:
        print(row)