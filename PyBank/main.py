
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

#create lists
total_months = []
total_profit = []
monthly_change = []

with open("budget_data.csv", "r") as csvfile:
    
    #create a path
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #skip column labels
    header = next(csvreader, None)
    
    #iterate through rows in budget data
    for row in csvreader:
        
        #append months and profit lists 
        total_months.append(row[0])
        total_profit.append(int(row[1]))
        
    #iterate through profits to get monthly changes
    for i in range(len(total_profit)-1):
        monthly_change.append(total_profit[i+1]-total_profit[i])

#calculate min and max values for monthly changes
max_decrease_val = min(monthly_change)
max_increase_val = max(monthly_change)

#calculate the greatest increase and decrease in profits (date and amount) over the entire period
max_increase_month = monthly_change.index(max(monthly_change)) + 1
max_decrease_month = monthly_change.index(min(monthly_change)) + 1 

#print statements
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_val))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_val))})")
