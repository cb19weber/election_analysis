# The data we need to retrieve.
# 1. Tthe total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of th eelection based on popular vote.

# Add dependencies (import modules)
from asyncore import write
import csv
import os

# Assign variables for the file to load and the file to save and the paths.
file_to_load = os.path.join("resources","election_results.csv")
file_to_save = os.path.join("analysis","election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

#2. Create a list of candidates in the election who received votes.
candidate_options = []
# Create a dictionary to hold total votes for each candidate.
candidate_votes = {}

# Open the election results and read the file.
# Files can be opened like this:
# open(file_to_load, "r")
with open(file_to_load) as election_data:

# Perform analysis: read and analyze the data here.
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Read the data in the CSV file
    for row in file_reader:
        
        #2. Get list of candidate names and accumulate total_votes
        total_votes += 1
        candidate_name = row[2]
        #candidate_votes = {"candidate_name1": votes, "candidate_name2": votes, "candidate_name3": votes}
        # Capture only the unique names from the dataset
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        #4. Accumulate the total votes for each candidate.
        candidate_votes[candidate_name] += 1

print(candidate_votes)

# Write data analysis to the created file.
# Files can be opened like this:
# open(file_to_save, "w")
with open(file_to_save,"w") as txt_file:
    txt_file.write("Counties in the Election\n")
    txt_file.write("-"*25 + "\n")
    txt_file.write(f"{total_votes:,}\n")
    txt_file.write(f"{candidate_options}")

# Close the file.
# election_data.close()
# outfile.close()