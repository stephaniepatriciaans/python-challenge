import os
import csv

# Initialize variables
total = 0
candidates = []
votes = {}
winner = ""
winner_votes = 0
analysis = ""

#giving the path the csv folder that want to be directed
election_csv = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(election_csv) as file:
    reader = csv.reader(file, delimiter=",")

     # Read the header row first (skip this part if there is no header)
    header = next(reader)

     # Read through each row of data after the header
    for row in reader :
        
        # vote count
        total += 1

        #print(row)
        #candidate's name 
        candidate = row[2]

        # If the candidate is not already in the list, add them
        if candidate not in votes:
            votes[candidate] = 0

        # Increment the candidate's vote count
        votes[candidate] += 1

# Print  header
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total}")
print("-------------------------")

#calculation won
for candidate, vote in votes.items():
    percentage = (vote / total) * 100
    
    #print candidate
    print(f"{candidate}: {percentage:.3f}% ({vote})")

    # candidate votes > current winner
    if vote > winner_votes:
        winner_votes = vote
        winner = candidate
#print winner
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")