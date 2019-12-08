import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
output_path = os.path.join("Resources","election_data.csv")


with open(output_path,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    candidate = []
    votes = []
    name= []

    for row in csvreader:
        candidate.append(row[2])
    candidate_count = [[x,candidate.count(x)] for x in set(candidate)]

    for row in candidate_count:
        name.append(row[0])
        votes.append(row[1])

    candidate_zip = zip(name,votes)
    candidate_list = list(candidate_zip)
    winner = max(votes)

    for row in candidate_list:
        if row[1] == winner:
            winner_name = row[0]

total_votes = len(candidate)
correy_total = candidate.count('Correy')
correy_percent=int(correy_total)/int(total_votes)

khan_total = candidate.count('Khan')
khan_percent = int(khan_total)/int(total_votes)

Li_total = candidate.count('Li')
Li_percent = int(Li_total)/int(total_votes)

Tooley_total = candidate.count("O'Tooley")
Tooley_percent = int(Tooley_total)/int(total_votes)

output_file = os.path.join("election_data.csv")

print(f"Election Results")
print("-------------------------")
print(f"Total Votes:  + {total_votes}")
print("-------------------------")
print(f"Khan : {khan_percent:.3%} ({khan_total})")
print(f"Correy : {correy_percent:.3%} ({correy_total})")
print(f"Li : {Li_percent:.3%} ({Li_total})")
print(f"O'Tooley : {Tooley_percent:.3%} ({Tooley_total})")
print(f"------------------------")
print(f"Winner : {winner_name}")