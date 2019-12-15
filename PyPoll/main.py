#Dependencies
import os
import csv

globalReader = []
#Specify file path
csvpath = os.path.join("election_data.csv")
output_file = "election_results.txt"

with open(csvpath, newline= "") as csvfile:
	#Read header row
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
most_votes = 0	
		
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
		
		
khan_percent = round((khan_votes/(len(votes) - 1) * 100), 3)
correy_percent = round((correy_votes/(len(votes) - 1) * 100), 3)
li_percent = round((li_votes/(len(votes) - 1) * 100), 3)
otooley_percent = round((otooley_votes/(len(votes) - 1) * 100), 3)

#Calculate winner
candidate_totals = [khan_votes, correy_votes, li_votes, otooley_votes]
winner = ""

for total in candidate_totals:
	if khan_votes == max(candidate_totals):
		winner = "Khan"
	elif correy_votes == max(candidate_totals):
		winner == "Correy"
	elif li_votes == max(candidate_totals):
		winner = "Li"
	elif otooley_votes == max(candidate_totals):
		winner = "O'Tooley"
	
		

print("")
print("Election Results")
print("-----------------------")
print("Total Votes: " + str(len(votes)- 1))
print("-----------------------")
print("Khan: " + f"{khan_percent:3f}" + "%" + " (" + str(khan_votes) + ")")
print("Correy: " + f"{correy_percent:.3f}" + "%" + " (" + str(correy_votes) + ")")
print("Li: " + f"{li_percent:.3f}" + "%" + " (" + str(li_votes) + ")")
print("O'Tooley: " + f"{otooley_percent:.3f}" + "%" + " (" + str(otooley_votes) + ")")
print("-----------------------")
print("Winner: " + winner)
print("-----------------------")


with open(output_file, "w") as textfile:
	textfile.write("Election Results")
	textfile.write("\n")
	textfile.write("-----------------------")
	textfile.write("\n")
	textfile.write("Khan: " + f"{khan_percent:3f}" + "%" + " (" + str(khan_votes) + ")")
	textfile.write("\n")
	textfile.write("Correy: " + f"{correy_percent:.3f}" + "%" + " (" + str(correy_votes) + ")")
	textfile.write("\n")
	textfile.write("Li: " + f"{li_percent:.3f}" + "%" + " (" + str(li_votes) + ")")
	textfile.write("\n")
	textfile.write("O'Tooley: " + f"{otooley_percent:.3f}" + "%" + " (" + str(otooley_votes) + ")")
	textfile.write("\n")
	textfile.write("-----------------------")
	textfile.write("\n")
	textfile.write("Winner: " + winner)
	textfile.write("\n")
	textfile.write("-----------------------")

