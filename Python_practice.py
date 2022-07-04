user_input = "y"
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
                   {"county":"Denver", "registered_voters": 463353},
                   {"county":"Jefferson", "registered_voters": 432438}]

while user_input == "y":
    print(type(voting_data))
    print(voting_data)

    for county in voting_data:
        print(f"{county['county']} county has {county['registered_voters']:,} registered voters.")
    user_input = input("Do you want to add additional counties? ")
    if user_input == "y":
        county_add = input("Enter name of the county: ")
        voter_add = int(input("Enter the number of registered voters: "))
        voting_data.append({"county":county_add, "registered_voters":voter_add})

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes *100:.2f}% of the total votes.")
print(message_to_candidate)