# Import modules.
import os
import csv
from shutil import move

#Route path for .csv file.
csv_path = os.path.join("Resources", "election_data.csv")

#Establish Variables.
Tot_Votes = 0
Ind_Can = list()
Tot_Votes_Can_0 = 0
Tot_Votes_Can_1 = 0
Tot_Votes_Can_2 = 0
Winner = []

#Open/read the .csv file.
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    #Isolate the header.
    Header = next(csv_reader)

    #Basic For Loop to read through each row.
    for row in csv_reader:

        #Calculate the total votes.
        Tot_Votes += 1

        #List of candidates voted for.
        Candidate = row[2]
        if Candidate not in Ind_Can:
            Ind_Can.append(Candidate)

        #Calculate the total number of votes for each candidate.
        if Candidate == "Charles Casper Stockham":
            Tot_Votes_Can_0 += 1
            
        if Candidate == "Diana DeGette":
            Tot_Votes_Can_1 += 1

        if Candidate == "Raymon Anthony Doane":
            Tot_Votes_Can_2 += 1

        #Calculate the percentage of votes per candidate.
        Perc_Can_0 = "{:.3f}".format((Tot_Votes_Can_0 / Tot_Votes) * 100)
        Perc_Can_1 = "{:.3f}".format((Tot_Votes_Can_1 / Tot_Votes) * 100)
        Perc_Can_2 = "{:.3f}".format((Tot_Votes_Can_2 / Tot_Votes) * 100)

        #Calculate the winner of the election based on popular vote.
        if Perc_Can_0 > Perc_Can_1:
            winner = "Charles Casper Stockham"
        elif Perc_Can_1 > Perc_Can_2:
            winner = "Diana DeGette"
        elif Perc_Can_2 > Perc_Can_0:
            winner = "Raymon Anthony Doane"

#Output Analysis.
print("Election Results")
print("-------------------------")
print(f"Total Votes: {Tot_Votes}")
print("-------------------------")
print(f"{Ind_Can[0]}: {Perc_Can_0}% ({Tot_Votes_Can_0})")
print(f"{Ind_Can[1]}: {Perc_Can_1}% ({Tot_Votes_Can_1})")
print(f"{Ind_Can[2]}: {Perc_Can_2}% ({Tot_Votes_Can_2})")
print("-------------------------")
print(f"Winner: {winner}")

#Export results to text file.
Export = open("Results.txt", "w")

L1 = "Election Results"
L2 = "-------------------------"
L3 = str(f"Total Votes: {Tot_Votes}")
L4 = "-------------------------"
L5 = str(f"{Ind_Can[0]}: {Perc_Can_0}% ({Tot_Votes_Can_0})")
L6 = str(f"{Ind_Can[1]}: {Perc_Can_1}% ({Tot_Votes_Can_1})")
L7 = str(f"{Ind_Can[2]}: {Perc_Can_2}% ({Tot_Votes_Can_2})")
L8 = "-------------------------"
L9 = str(f"Winner: {winner}")
Export.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(L1, L2, L3, L4, L5, L6, L7, L8, L9))

Export.close()

move("Results.txt", "Analysis")