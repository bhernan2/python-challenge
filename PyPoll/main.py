# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.


#imoport modules
import os
import csv

#create path
election_data=os.path.join("election_data.csv")

#set total vote variable
total_votes = 0
#set candidate variables
correy = 0
khan = 0
li = 0 
otooley = 0 
