# Import modules.
import os
import csv
from shutil import move

#Route path for .csv file.
csv_path = os.path.join("Resources", "budget_data.csv")


#Establish variables.
Tot_Mon = 0
Tot_ProLos = 0
Dif = 0
Chg = 0
Date = []
ProLos = []

#Open/read the .csv file.
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    #Isolate the header.
    Header = next(csv_reader)

    #Trace changes.
    Fir_Row = next(csv_reader)
    Tot_Mon += 1
    Tot_ProLos += int(Fir_Row[1])
    Dif = int(Fir_Row[1])

    #Basic For Loop to read through each row.
    for row in csv_reader:
        
        #Manage dates for later callback
        Date.append(row[0])

        #List calculated changes.
        Chg = int(row[1]) - Dif
        ProLos.append(Chg)
        Dif = int(row[1])

        #Caluclate average total profit/loss over the entire period.
        Avg_Chg = format(sum(ProLos)/len(ProLos), ".2f")

        #Calculate total months
        Tot_Mon += 1

        #Calculate total profits and losses over the entire period.
        Tot_ProLos = Tot_ProLos + int(row[1])

        #Calculate the greatest increase in profits.
        Grt_Inc = max(ProLos)
        Grt_Ind = ProLos.index(Grt_Inc)
        Grt_Date = Date[Grt_Ind]

        #Calculate the greatest decrease in profits.
        Grt_Dec = min(ProLos)
        Lst_Ind = ProLos.index(Grt_Dec)
        Lst_Date = Date[Lst_Ind]

#Output Analysis.
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {Tot_Mon}")
print(f"Total: ${Tot_ProLos}")
print(f"Average Change: ${Avg_Chg}")
print(f"Greatest Increase in Porfits: {Grt_Date} (${Grt_Inc})")
print(f"Greatest Decrease in Profits: {Lst_Date} (${Grt_Dec})")

#Export results to text file.
Export = open("Results.txt", "w")

L1 = "Financial Analysis"
L2 = "----------------------------"
L3 = str(f"Total Months: {Tot_Mon}")
L4 = str(f"Total: ${Tot_ProLos}")
L5 = str(f"Average Change: ${Avg_Chg}")
L6 = str(f"Greatest Increase in Porfits: {Grt_Date} (${Grt_Inc})")
L7 = str(f"Greatest Decrease in Profits: {Lst_Date} (${Grt_Dec})")
Export.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(L1, L2, L3, L4, L5, L6, L7))

Export.close()


move("Results.txt","Analysis")
