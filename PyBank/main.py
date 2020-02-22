
# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The average of the changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period


#libraries needed
import os
import csv

# file location
budget_df=os.path.join("..", "PyBank", "budget_data.csv")
budget_df

# create empty list for total months 
months []
total_pl = []
total_months = 0
total_profit = 0 

# open csv in reader mode 
with open("budget_data.csv", "r") as csvfile:
    #store budget_df data in csvreader 
    csvreader = csv.reader(csvfile, delimiter = ",")
    #skip column labels
    next(csvreader, None)
    #iterate through monthly data and calculate 
    for months in csvreader:
        total_months += 1
    print(f"Total Months: {str(total_months)}")
# Total Months: 86 

# Total profits
with open("budget_data.csv", "r") as csvfile:
    #store budget_df data in csvreader 
    csvreader = csv.reader(csvfile, delimiter = ",")
    #skip column labels
    next(csvreader, None)
    #iterate through monthly data
    for total_pl in csvreader:
        total_profit = total_profit + (int(total_pl[1]))
    print(f"Total Profit: {int(total_profit)}")
# Total Profit: 38382664
