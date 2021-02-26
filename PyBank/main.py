#(PyBank)

# Import
import os
import csv

# Variables
total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# Set Path
csvpath = os.path.join(r"C:/Users/stuar/bootcamp1/python_homework/Python-Challenges/PyBank/Resources/budget_data.csv")

# Open and Read CSV File
with open(csvpath, newline='') as csvfile:
    
    # CSV Reader Specifies Delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read Header Row First, Skip This Step if No Header)
    csv_header = next(csvreader)
    row = next(csvreader)
    
    # Calculate Total Number Of Months, Net Amount Of "Profit/Losses" & Set Variables For Rows
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    # Read Each Row Of Data After The Header
    for row in csvreader:
        
        # Calculate Total Number Of Months Included
        total_months += 1
        # Calculate Net Amount Of "Profit/Losses" Over The Entire Duration
        net_amount += int(row[1])

        # Calculate Change From Current Month To Previous Month
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        # Calculate The Greatest Increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        # Calculate The Greatest Decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
    # Calculate The Average & The Date
    average_change = sum(monthly_change)/ len(monthly_change)
    
    highest = max(monthly_change)
    lowest = min(monthly_change)

# Print Analysis
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")

# Specify File To Write To
output_file = os.path.join(r"C:/Users/stuar/bootcamp1/python_homework/Python-Challenges/PyBank/analysis/budget_data.txt")

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w',) as txtfile:

# Write New Data
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_amount}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")