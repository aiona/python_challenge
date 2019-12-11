#Dependencies
import os
import csv

globalReader = []
#Specify file path
csvpath = os.path.join("budget_data.csv")

with open(csvpath, newline= "") as csvfile:
	#Read header row
	#csvheader = ['Date','Profit/Losses']
	
	#print(f"CSV Header: {csvheader}")
	
	csvreader = csv.reader(csvfile, delimiter=',')
	print(csvreader)
	csvheader = next(csvreader)
	
	 
	reader = list(csvreader)
	 
	#Read each row of data	
	for rows in csvreader:
		print(rows)
		
print ("")
print("Financial Analysis")
print("-------------------")


#Calculate the total number of months
months = list(csv.reader(open('budget_data.csv')))
month_count = len(months)
print("Total Months: " + str(len(months)- 1))

total_profit = 0
previous_profit = 867884
sum_change = 0
#greatest_increase =
#greatest_decrease = 
profit_change = 0
profit_changes = []

#Loop through rows
for row in reader:
	
	#Calculate the total profit - profit[0] + profit[1] + profit[2] + ...
	total_profit += int(row[1])	
		
	#total_profit = total_profit + int(row['Profit/Losses']) How do I get this value out?
	
	#Calculate average change
	profit_change = int(row[1]) - previous_profit
	
	#Calculate sum_change
	sum_change += profit_change
	
	#profit_changes.append(int(row[1]))
	
	previous_profit = int(row[1])
	#Calculate profit change: profit[1]- profit[0]
	#average change = sum(profit_changes)/len(profit_changes)
	
	
	#Calculate greatest increase in profits
	#compare greatest increase to profit change
	#maximum of profit_changes
	#profit_changes.append(int(row[1]))

	#Calculate greatest decrease in profits
	#compare greatest_decrease to profit_change
	
print("Total Profits: " +str(total_profit))
print("Average Change: ")
print("Greatest Increase in Profits: ")
print("Greatest Decrease in Profits: ")

