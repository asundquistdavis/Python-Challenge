# Import OS and use it to make a relative path to csv file
import os
csvpath = os.path.join('Resources', 'budget_data.csv')

# Initialize global variables
profits = [] # list to store all profits
total_profit = 0 # sum of all profits
change_in_profits = [] # list to store change in profits, month to month
months = [] # list to store the month/year

# Import CSV and open csv file
import csv
with open(csvpath) as csvfile:
    
    # Use CSV to read file
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip over first row which has headers info
    header = next(csvreader)

    # Go row by row in csvfile and convert the second value into an integer and store it as the profit - the first vaule is stored as a string
    for row in csvreader:
        profits.append(int(row[1]))
        months.append(row[0])

# For each profit in the list, profits, do the following:
for index, profit in enumerate(profits):
    
    # Add profit to total profits
    total_profit += profit
 
    # Calculate and store the change in profit from previous month to current month
    if index == 0:
        # Change in profits is not defined for first month (we do not know prevous profis) so set as zero - this is just a place holder!
        change_in_profits.append(0)
        
    else:    
        # Current month's change in profits is equal to current month's profit minus previous month's profit
        change_in_profits.append(profit - profits[index - 1])

# Number of months is the length of the profits list
total_months = len(profits)

# Average change in profits = total change in profits divided by number of months we have data for change in profits, which is one less than the total number of months
average_change = round((profits[total_months - 1] - profits[0])/(total_months - 1), 2)

# Greatest increase in profits is equal to the max of the change in profits list
greatest_increase = max(change_in_profits)

# Month with greatest increase:
i_max = change_in_profits.index(greatest_increase)
month_max = months[i_max]

# Greatest decrease in profits is equal to the min of the change in profits list
greatest_decrease = min(change_in_profits)

# Month with greatest decrease:
i_min = change_in_profits.index(greatest_decrease)
month_min = months[i_min]

# Print results to console
print('Financial Analysis')
print('------------------------------------------------------')
print(f'Total Months: {total_months}')
print(f'Total Profit: ${total_profit}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {month_max} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {month_min} (${greatest_decrease})')

# Create new folder and file to store results
txtpath = os.path.join('Analysis', 'financial_analysis.txt')
with open(txtpath, 'w') as txtfile:
    txtfile.write('Financial Analysis\n')
    txtfile.write('------------------------------------------------------\n')
    txtfile.write(f'Total Months: {total_months}\n')
    txtfile.write(f'Total Profit: ${total_profit}\n')
    txtfile.write(f'Average Change: ${average_change}\n')
    txtfile.write(f'Greatest Increase in Profits: {month_max} (${greatest_increase})\n')
    txtfile.write(f'Greatest Decrease in Profits: {month_min} (${greatest_decrease})')
