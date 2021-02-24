# Read csv file budget_data
import os
import csv

# Set the path for file
csvpath = os.path.join("..", "PyBank", "Resources", "03_PyBank_Resources_budget_data.csv")

# Set variables
num_months = 0
net_total = 0
num_profit = 0
total_change = 0
increase = 0
decrease = 0

# Open the csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Set the header row & the first row for the profit
    csv_header = next(csvreader)
    
    # Create loop with to read each row of data after the header
    for row in csvreader:
    
        # Calculate the total number of months included in the dataset
        num_months += 1
        
        # Calculate the net total amount of "Profit/Losses" over the entire period
        net_total += int(row[1])
        
        # Calculate the differences
        if num_months == 1:
        
            profit1 = int(row[1])

        elif num_months > 1:
        
            profit2 = int(row[1])
            
            # Identify the count for later use (calculating average)
            num_profit += 1
            
            changes = profit2 - profit1
        
            total_change = total_change + changes
        
            # Update profit1
            profit1 = int(row[1])
            
            # Calculate the greatest increase & decrease in profits and identify the month & year
            if changes > increase:
                
                increase = changes
                increase_date = row[0]
            
            elif changes < decrease:
                
                decrease = changes
                decrease_date = row[0]
    
    # Calculate average change
    average_change = total_change / num_profit
  
  
  
# Print the results to the terminal
print("Financial Analysis")
print("----------------------------------")
print("Total Months: " + str(num_months))
print("Total: $" + str(net_total))
print("Average Change: $" + str(round(average_change,2)))
print("Greatest Increase in Profits: " + increase_date + " ($" + str(round(increase,2)) + ")")
print("Greatest Decrease in Profits: " + decrease_date + " ($" + str(round(decrease,2)) + ")")

# Export the results into a text file
with open("Analysis/PyBank_analysis.txt", "w") as txt_file:
    
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------------\n")
    txt_file.write("Total Months: " + str(num_months) + "\n")
    txt_file.write("Total: $" + str(net_total) + "\n")
    txt_file.write("Average Change: $" + str(round(average_change,2)) + "\n")
    txt_file.write("Greatest Increase in Profits: " + increase_date + " ($" + str(round(increase,2)) + ")\n")
    txt_file.write("Greatest Decrease in Profits: " + decrease_date + " ($" + str(round(decrease,2)) + ")\n")

    
output_file = os.path.join("Analysis", "PyBank_analysis.txt")
