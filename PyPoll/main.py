#Dependencies
import os
import csv

globalReader = []
#Specify file path
csvpath = os.path.join("election_data.csv")

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

#Calculate total votes
votes = list(csv.reader(open('election_data.csv')))
vote_count = len(votes) - 1
		
khan_votes = 0
correy_votes = 0
li_votes = 0
li_percent = 0
otooley_votes = 0
otooley_percent = 0		
		
#Loop through rows
for row in reader:

	if row[2] == "Khan":
		khan_votes += 1
		
	elif row[2] == "Correy":
		correy_votes += 1
				
	elif row[2] == "Li":
		li_votes += 1
				
	else:
		otooley_votes +=1 		
		
		
khan_percent = khan_votes//vote_count
correy_percent = correy_votes//vote_count
li_percent = li_votes//vote_count
otooley_percent = otooley_votes//vote_count

		

print("Election Results")
print("-----------------------")

print("Total Votes: " + str(len(votes)- 1))
print("-----------------------")
print("Khan:" + str(khan_percent) + "%" + " (" + str(khan_votes) + ")")
print("Correy:" + str(correy_votes))
print("Li:" + str(li_votes))
print("O'Tooley:" + str(correy_votes))
print("-----------------------")
print("-----------------------")
print("Winner: ")
print("-----------------------")


