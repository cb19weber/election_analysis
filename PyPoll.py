# The data we need to retrieve.
# 1. Tthe total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of th eelection based on popular vote.

# Add dependencies (import modules)
import csv
import os

# Assign variables for the file to load and the file to save and the paths.
file_to_load = os.path.join("resources","election_results.csv")
file_to_save = os.path.join("analysis","election_analysis.txt")

# Open the election results and read the file.
# Files can be opened like this:
# open(file_to_load, "r")
with open(file_to_load) as election_data:

# Perform analysis: read and analyze the data here.
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    # for row in file_reader:
    #    print(row)

# Write data analysis to the created file.
# Files can be opened like this:
# open(file_to_save, "w")
with open(file_to_save,"w") as txt_file:
    txt_file.write("Counties in the Election\n")
    txt_file.write("-"*25 + "\n")
    txt_file.write("Arapahoe\n")
    txt_file.write("Denver\n")
    txt_file.write("Jefferson")

# Close the file.
# election_data.close()
# outfile.close()