# Import OS and create a relative path to election data csv file
import os
csvpath = os.path.join('Resources', 'election_data.csv')

# Import CSV
import csv

# Create some variables
votes = [] # list to store name of canadate voted for
stockham_votes = 0 # number of votes for Stockham
degette_votes = 0 # " DeGette
doane_votes = 0 # " Doane
invalid_votes = 0 # Number of votes that doesn't match one of the canadates - should be zero (for valadation purposes)
winner = '' # String that contains the naim of the winner

# Open election_data.csv
with open(csvpath) as csvfile:
    
    # Use csv to read election_data.csv file
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip first row with header strings
    next(csvreader)

    # Go row by row in csvreader and save the canadate to list
    for ballot in csvreader:
        votes.append(ballot[2])

# Go through votes and count ballots cast for each canadate
for vote in votes:
    if vote == 'Charles Casper Stockham':
        stockham_votes += 1
    elif vote == 'Diana DeGette':
        degette_votes += 1
    elif vote == 'Raymon Anthony Doane':
        doane_votes += 1
    else:
        invalid_votes += 1

# Total number of votes is the length of the votes list
total_votes = len(votes)

# Percent of votes = (# of votes for canadate) / (total number of votes) * 100
stockham_percent = round((stockham_votes / total_votes) * 100, 3)
degette_percent = round((degette_votes / total_votes) * 100, 3)
doane_percent = round((doane_votes / total_votes) * 100, 3)

# Pick winner with If statement:
if stockham_votes > degette_votes and stockham_votes > doane_votes:
    winner = 'Charles Casper Stockham'
if degette_votes > stockham_votes and degette_votes > doane_votes:
    winner = 'Dianna DeGette'
if doane_votes > stockham_votes and doane_votes > degette_votes:
    winner = 'Raymon Anothy Doane'

# Print results results to terminal
print('Election Results')
print('------------------------------')
print(f'Charles Capser Stockham: {stockham_percent}% ({stockham_votes})')
print(f'Diana DeGette: {degette_percent}% ({degette_votes})')
print(f'Raymon Anthony Doane: {doane_percent}% ({doane_votes})')
print('------------------------------')
print(f'Winner: {winner}')

# Create a path to txtfile
txtpath = os.path.join('Analysis', 'elction_reults.txt')

# Open txt file
with open(txtpath, 'w') as txtfile:
    txtfile.write('Election Results\n')
    txtfile.write('------------------------------\n')
    txtfile.write(f'Charles Capser Stockham: {stockham_percent}% ({stockham_votes})\n')
    txtfile.write(f'Diana DeGette: {degette_percent}% ({degette_votes})\n')
    txtfile.write(f'Raymon Anthony Doane: {doane_percent}% ({doane_votes})\n')
    txtfile.write('------------------------------\n')
    txtfile.write(f'Winner: {winner}')