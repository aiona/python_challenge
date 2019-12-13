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
previous_change = 0
greatest_increase_month = ""
#greatest_increase_month = largest value in profit_changes
#greatest_decrease_month = smallest value in profit_changes
profit_change = 0
profit_changes = []
months = []


#Loop through rows
for row in reader:
	
	#Calculate the total profit - profit[0] + profit[1] + profit[2] + ...
	total_profit += int(row[1])	
			
	#Calculate profit change
	profit_change = int(row[1]) - int(previous_profit)
	print(profit_change)
	profit_changes.append(profit_change)
	months.append(row[0])
	
	previous_profit = row[1]
	#min_month = 
	#max_month = 
	
	#sorting a list in python 
	#
	
	#compare current change with previous
	#Help!

for change in profit_changes:
	if profit_change > previous_change:
		greatest_increase_month=(row[0])			
	
	previous_profit = int(row[1])
	
	#Calculate profit change month profit[1]- profit[0]
	
	
#Calculate average change 
average_change = sum(profit_changes)/(len(profit_changes)-1)

#Keep track of months
#index of min month, index max month	
	
#compare greatest increase to profit change
#maximum of profit_changes
#if profit_change[n] > profit_change[n-1]
	#then greatest_profit_month

#Calculate greatest decrease in profits
#compare greatest_decrease to profit_change
 	
print("Total: " +str(total_profit))
print("Average Change: $" + f"{average_change:.2f}")
print("Greatest Increase in Profits: " + greatest_increase_month +  "($" + str(max(profit_changes)) + ")")
print("Greatest Decrease in Profits: " + "($" + str(min(profit_changes)) + ")")

