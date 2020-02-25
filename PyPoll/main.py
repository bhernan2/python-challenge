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

#calculate candidate vote percentages
correy_percent = (correy/total_votes)*100
khan_percent = (khan/total_votes)*100
li_percent = (li/total_votes)*100
otooley_percent = (otooley/total_votes)*100

#print statements
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Correy: {correy_percent: .3f}% ({correy})")
print(f"Khan: {khan_percent: .3f}% ({khan})")
print(f"Li: {li_percent: .3f}% ({li})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley})")
print(f"----------------------------")
print(f"Winner: {winner}")
print(f"----------------------------")

#export a text file with the results
output_path = os.path.join("Election_Results.txt")
output_path

with open("Election_Results.txt","w", newline='') as file:
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy})")
    file.write("\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khan})")
    file.write("\n")
    file.write(f"Li: {li_percent:.3f}% ({li})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write(f"----------------------------")

