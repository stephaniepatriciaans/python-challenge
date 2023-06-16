import os
import csv

#Initialize the variable
Total_Months = 0
Net_Total = 0
previous = 0
change_list = []
change = 0
increase = ["", 0]
decrease = ["", 0]

#giving the path the csv folder that want to be directed
pybank_csv = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(pybank_csv) as file:
    reader = csv.reader(file, delimiter=",")
    
    # Read the header row first (skip this part if there is no header)
    header = next(reader)
    
    # Read through each row of data after the header
    for row in reader : 
        
        #count total month
        Total_Months += 1
        
        #count net total
        Net_Total += int(row[1])
        
        #count change profit/loss
        change = int(row[1]) - previous
        
        #add change
        change_list.append(change)
        
        #update change
        previous = int(row[1])
        
        #current = greatest increase
        if change > increase[1]:
            increase[0] = row[0]
            increase[1] = change
        
        #current = greatest decrease
        if change < decrease[1]:
            decrease[0] = row[0]
            decrease[1] = change
            
# count average
average = sum(change_list[1: ]) / (Total_Months-1)

#print
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Net_Total}")
print(f"Average Change: ${average: .2f}")
print(f"Greatest Increase in Profits: {increase[0]} ${increase[1]}")
print(f"Greatest Decrease in Profits: {decrease[0]} ${decrease[1]}")