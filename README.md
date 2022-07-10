# Python-Challenge
This is for the Python challenge homework assignment which explores Python's ability to read and write to csv files using the CSV module. The challenge includes two parts:
- PyBank reads financial data from a csv file, analyses it and writes a txt file with a summary of the analysis. 
- PyPoll reads election ballots data from a csv file and counts total votes. It returns a txt file with the election results. 
## Contents
- PyBank:
    - Analysis
        - financial_analysis.text: this is the file that main.py writes.
    - Reasources
        - budget_data.csv: this is the file provided by Trilogy Education Services as data for the Pybank Challenge.
    - main.py: this is the main script that analyses the budget_data.csv file.
- PyPoll:
    - Analysis
        - election_results.txt: this is the file that main.py writes.
    - Resources
        - election_data.csv: this is the file provided by Trilogy Education Services for the Pypoll Challenge.
    - main.py: this is the main script that determines the election results.
- .gitignore: gitignore is configured for Python as that is the only coding language used in this challenge.
## Approach and Further Considerations
### Reading File
In both sub-challenges, the csv module is used to read the csv files provided. In the original approach for solving PyBank, within the `with open` statement each line of the csv file is stored as an element in two seperates list - months and profits. A better way to store this data would be a one dictionary with two keys - months and profits and lists as elements. This approach is favorable as it resembles the more popular dataframe approach. 
### Analysis
In the PyBank sub-challenge, one of the deliverables is to record the change in profits from month to month. Since profit data in not know for months outside the range provided, the change in profit for the first month is not well defined. `0` is used as a placed holder, however it is worth noting that this is not the true value; the value is simply just unkown. This choice was made to keep the indices of all the lists consistant. 
### Writing to Files
The files are writen using a simple `with open(file, 'w')` and the result is a simple txt file. A more sophisticated approch would be to write to a mark down file or a jupyter notebook. This would increase the readability. However, given the scope of the challenge, the txt files get the job done.