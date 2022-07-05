# The data we need to retrieve.
# 1. Tthe total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of th eelection based on popular vote.

# Import modules
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources","election_results.csv")
file_to_save = os.path.join("analysis","election_analysis.txt")

# Open the election results and read the file.
# election_data = open(file_to_load,'r')
with open(file_to_load) as election_data:

# To do: perform analysis.
    print(election_data)

# Using the open() function with the 'w' mode we will write data to the file.
open(file_to_save,"w")

# Close the file.
# election_data.close()