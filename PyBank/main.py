#Dependencies
import os
import csv

globalReader = []
#Specify file path
csvpath = os.path.join("budget_data.csv")
output_file = "budget_analysis.txt"

with open(csvpath, newline= "") as csvfile:
	#Read header row
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
greatest_decrease_month = ""
profit_change = 0
profit_changes = []
months = []


#Loop through rows
for row in reader:
	
	#Calculate the total profit - profit[0] + profit[1] + profit[2] + ...
	total_profit += int(row[1])	
			
	#Calculate profit change
	profit_change = int(row[1]) - int(previous_profit)
	#print(profit_change)
	profit_changes.append(profit_change)
	months.append(row[0])
	
	previous_profit = row[1]
	
	for pc in profit_changes:
		if profit_change == max(profit_changes):
			greatest_increase_month = row[0]
		if profit_change == min(profit_changes):
			greatest_decrease_month = row[0]


if max(profit_changes) == int(row[1]):
	print(greatest_increase_month)	
	
#Calculate average change 
average_change = sum(profit_changes)/(len(profit_changes)-1)
 	
print("Total: " +str(total_profit))
print("Average Change: $" + f"{average_change:.2f}")
print("Greatest Increase in Profits: " + greatest_increase_month +  " ($" + str(max(profit_changes)) + ")")
print("Greatest Decrease in Profits: " + greatest_decrease_month + " ($" + str(min(profit_changes)) + ")")

#Output files

with open(output_file, "w") as textfile:
	textfile.write("Financial Analysis")
	textfile.write("\n")
	textfile.write("-------------------")
	textfile.write("\n")
	textfile.write("Total Months: " + str(len(months)))
	textfile.write("\n")
	textfile.write("Total: " + str(total_profit))
	textfile.write("\n")
	textfile.write("Average Change: $" + f"{average_change:.2f}")
	textfile.write("\n")
	textfile.write("Greatest Increase in Profits: " + greatest_increase_month +  " ($" + str(max(profit_changes)) + ")")
	textfile.write("\n")
	textfile.write("Greatest Decrease in Profits: " + greatest_decrease_month + " ($" + str(min(profit_changes)) + ")")
	


