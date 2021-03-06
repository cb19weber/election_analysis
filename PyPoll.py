# Add dependencies (import modules)
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

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

election_results = (
    f"\nElection Reults\n" + 
    f"-"*25 + "\n"
    f"Total Votes: {total_votes:,}\n" + 
    f"-"*25 + "\n")
print(election_results)

# Write data analysis to the created file.
# Files can be opened like this:
# open(file_to_save, "w")
with open(file_to_save,"w") as txt_file:
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate:
        votes = candidate_votes[candidate_name]
        # 3. Calulate the percentage of votes:
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes:
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})")
        print(candidate_results)
        txt_file.write(candidate_results + "\n")
        # 5. Determine the winning candidate:
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_candidate = candidate_name
            winning_count = votes
            winning_percentage = vote_percentage

    winning_candidate_summary = (
        f"-"*25 + "\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n" + 
        f"-"*25 + "\n")
    txt_file.write(winning_candidate_summary)
    print(winning_candidate_summary)
