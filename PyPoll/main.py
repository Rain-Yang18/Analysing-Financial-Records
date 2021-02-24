# Read csv file budget_data
import os
import csv

# Set the path for file
csvpath = os.path.join("Resources", "03_PyPoll_Resources_election_data.csv")

# Set variables, list & dict
total_votes = 0
name_list = []
candidate1_votes = 0
candidate2_votes = 0
candidate3_votes = 0
candidate4_votes = 0

candidates = {}

# Open the csv
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Set the header row
    csv_header = next(csvreader)
     
    # Create loop with to read each row of data after the header
    for row in csvreader:
    
        # The total votes
        total_votes += 1
        
        # Identify the unique name list
        if row[2] not in name_list:
        
            name_list.append(row[2])
            
        # Calculate the total number of votes each cadidate won
        if row[2] == name_list[0]:
            
            candidate1_votes += 1
            
        elif row[2] == name_list[1]:
        
            candidate2_votes += 1
            
        elif row[2] == name_list[2]:
        
            candidate3_votes += 1
            
        else:
        
            candidate4_votes += 1

        # Calculate the winner of the election
        if candidate1_votes > candidate2_votes and candidate1_votes > candidate3_votes and candidate1_votes > candidate4_votes:
        
            winner = name_list[0]
            
        elif candidate2_votes > candidate1_votes and candidate2_votes > candidate3_votes and candidate2_votes > candidate4_votes:
        
            winner = name_list[1]
            
        elif candidate3_votes > candidate1_votes and candidate3_votes > candidate2_votes and candidate3_votes > candidate4_votes:
        
            winner = name_list[2]
            
        elif candidate4_votes > candidate1_votes and candidate4_votes > candidate2_votes and candidate4_votes > candidate3_votes:
        
            winner = name_list[3]
            
    # Calculate the % for each candidate & format them in %
    candidate1_percent = candidate1_votes / total_votes
    percent1 = "{:.3%}".format(candidate1_percent)
    
    candidate2_percent = candidate2_votes / total_votes
    percent2 = "{:.3%}".format(candidate2_percent)
    
    candidate3_percent = candidate3_votes / total_votes
    percent3 = "{:.3%}".format(candidate3_percent)
    
    candidate4_percent = candidate4_votes / total_votes
    percent4 = "{:.3%}".format(candidate4_percent)
    
    # Put all results into the dic for printing them out
    candidates = {
        "name": name_list,
        "percent": [percent1, percent2, percent3, percent4],
        "votes": [candidate1_votes, candidate2_votes, candidate3_votes, candidate4_votes]
    }
  
  
# Print the results on terminal
print("Election Results")
print("-------------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------------")
print(f'{candidates["name"][0]}: {candidates["percent"][0]} ({candidates["votes"][0]})')
print(f'{candidates["name"][1]}: {candidates["percent"][1]} ({candidates["votes"][1]})')
print(f'{candidates["name"][2]}: {candidates["percent"][2]} ({candidates["votes"][2]})')
print(f'{candidates["name"][3]}: {candidates["percent"][3]} ({candidates["votes"][3]})')
print("-------------------------------")
print("Winner: " + winner)
print("-------------------------------")
    

# Export the results into a text file
with open("Analysis/PyPoll_analysis.txt", "w") as txt_file:
    
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------------\n")
    txt_file.write("Total Votes: " + str(total_votes) + "\n")
    txt_file.write("-------------------------------\n")
    txt_file.write(f'{candidates["name"][0]}: {candidates["percent"][0]} ({candidates["votes"][0]})\n')
    txt_file.write(f'{candidates["name"][1]}: {candidates["percent"][1]} ({candidates["votes"][1]})\n')
    txt_file.write(f'{candidates["name"][2]}: {candidates["percent"][2]} ({candidates["votes"][2]})\n')
    txt_file.write(f'{candidates["name"][3]}: {candidates["percent"][3]} ({candidates["votes"][3]})\n')
    txt_file.write("-------------------------------\n")
    txt_file.write("Winner: " + winner + "\n")
    txt_file.write("-------------------------------\n")

output_file = os.path.join("Analysis", "PyPoll_analysis.txt")
