#Import modules
import os
import csv

# Total Vote Counter
total_votes = 0

# Candidate Options and Vote Counters
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

#Candidates who received votes variables
khan_votes = 0
correy_votes = 0
li_votes = 0
o_tooley_votes = 0

#Candidates percentage of votes each candidate won variables
khan_percent = 0
correy_percent = 0
li_percent = 0
o_tooley_percent = 0


#Path for file

os.chdir(os.path.dirname(os.path.abspath(__file__)))

csvpath = os.path.join("..", "PyPoll", "election_data.csv")


# Read the csv and convert it into a list of dictionaries

with open("election_data.csv") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile, None)
    #header
    #count each vote for each candidate
    for row in csvreader:
        total_votes += 1
        if row[2] == 'Khan':
            khan_votes += 1
        else if row[2] == 'Correy':
            correy_votes += 1
        else if row[2] == 'Li':
            li_votes += 1
        else:
            o_tooley_votes += 1
            
#Calculate percentages of votes each candidate won

khan_percent = (khan_votes/total_votes)*100
correy_percent = (correy_votes/total_votes)*100
li_percent = (li_votes/total_votes)*100
o_tooley_percent = (o_tooley_votes/total_votes)*100

#Candidate winner

if int(khan_votes) > int(correy_votes) and int(khan_votes) > int(li_votes) and int(khan_votes) > int(o_tooley_votes):
    winner = "Khan"
else if int(correy_votes) > int(khan_votes) and int(correy_votes) > int(li_votes) and int(correy_votes) > int(o_tooley_votes):
    winner = "Correy"
else if int(li_votes) > int(correy_votes) and int(li_votes) > int(khan_votes) and int(li_votes) > int(o_tooley_votes):
    winner = "Li"
else:
    winner = "O'Tooley"
    
#Print results and export data

text_summary = """

Election Results
--------------------------
Total Vote: {total_votes}
--------------------------
Khan: {khan_percent:.3f}% ({khan_votes})
Correy: {correy_percent:.3f}% ({correy_votes})
Li: {li_percent:.3f}% ({li_votes})
O'Tooley: {o_tooley_percent:.3f}% ({o_tooley_votes})
--------------------------
Winner: {winner}
-------------------------- """.format(total_votes=total_votes, khan_percent=khan_percent, khan_votes=khan_votes, correy_percent=correy_percent, correy_votes=correy_votes, li_percent=li_percent, li_votes=li_votes, o_tooley_percent=o_tooley_percent, o_tooley_votes=o_tooley_votes, winner=winner)

print(text_summary)
#write summary to new file
with open('summary.txt', 'w') as outfile:
    outfile.write(text_summary)
