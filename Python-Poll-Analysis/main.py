#Dependencies
import os
import csv

#joining path
election_data = os.path.join(".","Resources", "election_data.csv")
print(os.getcwd())

# find net amount of profit and loss
voterID = []
county = []
candidate = []
winner_index = 0



# open and read csv
with open(election_data, newline="") as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first
    csv_header = next(csvfile)
    # skip header row
    print(f"Header: {csv_header}")
    
    #read through each row of data after header
    for i in csvreader:
        voterID.append(i[0])
        county.append(i[1])
        candidate.append(i[2])
    #finish read csv files
        
              
# calculate total number of vote
count_voterID = len(voterID)

#print total number of vote
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(count_voterID))
print("----------------------------")
    
# The percentage of votes each candidate won & The total number of votes each candidate won

#find out how many candidate in the file
candidateList = list(set(candidate))

#set count of each candidate
candidatecount = []

for i in range(len(candidateList)):
#format to Khan: 63.000% (2218231)
    output = (candidateList[i] + ":" + '{0:.3f}%'.format(round((candidate.count(candidateList[i]))/count_voterID*100), 0) + " (" + str(candidate.count(candidateList[i]))+")")
    print(output)

    candidatecount.append(candidate.count(candidateList[i]))

print("----------------------------")    

# find the winner
winner = max(candidatecount)

for i in range(len(candidateList)):
    if candidate.count(candidateList[i]) == winner:
        print("Winner:" + candidateList[i])


#start write output file
with open('election_analysis.txt', 'w') as file:
    file.write("----------------------------------------------------------\n")
    file.write("Election Analysis"+ "\n")
    file.write("----------------------------------------------------------\n")
    file.write("Total Votes: " + str(count_voterID) + "\n")
    file.write("----------------------------------------------------------\n")
    for i in range(len(candidateList)):
        file.write(candidateList[i] + ":" + '{0:.3f}%'.format(round((candidate.count(candidateList[1]))/count_voterID*100), 0) + " (" + str(candidate.count(candidateList[1]))+")" + "\n")
        if candidate.count(candidateList[i]) == winner:
            winner_index = i
    file.write("----------------------------------------------------------\n")
    file.write("Winner:" + candidateList[winner_index] + "\n")
    file.write("----------------------------------------------------------\n")           
# finish the write output file
