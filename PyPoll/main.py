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

with open("election_data.csv", "r") as csvfile:
    #create path
    csvreader = csv.reader(csvfile)
    #skip column labels
    header = next(csvreader, None)
    #iterate through rows in election data
    for row in csvreader:
        #calculate total votes
        total_votes +=1
        # calculations for if the candidates are found in column, count the times they appear 
        if row[2] == "Correy":
            correy +=1
        elif row[2] == "Khan":
            khan +=1
        elif row[2] == "Li":
            li +=1
        elif row[2] == "O'Tooley":
            otooley +=1

#make list for the candidates ["Correy", "Khan", "Li", "O'Tooley"]
#and make list for total candidate votes from the above variables
candidates =["Correy", "Khan", "Li", "O'Tooley"]
votes_for_candidates = [correy, khan, li, otooley]

#combine both lists in a defined dictionary 
#combine candidates and votes_for_candidates lists 
#output should be candidate names and their respective total votes
help(dict)
help(zip)
candidate_votes_dict = dict(zip(candidates,votes_for_candidates))
candidate_votes_dict
#get function help to determine candidate winner 
help(candidate_votes_dict.get)
#calcualte the candidate winner using the max and get functions
winner = max(candidate_votes_dict, key = candidate_votes_dict.get)



