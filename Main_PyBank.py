
# Dependencies
import csv
import os

# Files to Load
file_to_load = "./budget_data.csv"
file_to_output = "./budget_analysis.txt"

# Variables to Track
total_months = 0
total_revenue = 0
previous_revenue = 0
revenue_change = 0
total_revenue_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999]

revenue_changes = []

# Read Files
with open(file_to_load) as revenue_data:
    reader = csv.reader(revenue_data)
    header = next(reader)
    print(header)
    first_data_row = next(reader)
    total_months = total_months + 1
    previous_revenue = int(first_data_row[1])
    total_revenue =  total_revenue + previous_revenue

    print(total_revenue)
    print(first_data_row)
    print(first_data_row[0])
    print(first_data_row[1])

    # Loop through all the rows of data we collect
    for row in reader:
        print(row)
        # Calculate the totals
        total_months = total_months + 1
        print(total_months)

        current_revenue = int(row[1])
        total_revenue = total_revenue + current_revenue
        revenue_change = current_revenue - previous_revenue
        print(revenue_change)
        total_revenue_change = total_revenue_change + revenue_change
        print(total_revenue_change)
        print("total revenue change", total_revenue_change)
        
       #Calculate the total revenue


       # Keeping track of the changes
        revenue_change = current_revenue - previous_revenue
        print(revenue_change)

        # Reset the value of previous_revenue to the row I completed my analysis
        print(previous_revenue)
        print(greatest_decrease) 
        print(greatest_increase)
        # Determine the greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row[0]
            print(greatest_increase[0])
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row[0]
            #print(greatest_decrease[0])
        # Add to the total_revenue_change
        # Assign current revenue for next row
        previous_revenue = current_revenue

    #Set the Revenue average
    revenue_change_average = (total_revenue_change) / (total_months - 1)
    print("revenue_change_average", revenue_change_average)
    print(total_revenue)

    #Show Output
    print()
    print()
    print()
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: " + "$" + str(total_revenue))
    print("Average Change: " + "$" + str(round(revenue_change_average, 2)))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ") ")
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ") ")

#Output Files
with open(file_to_output, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total_revenue))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(revenue_change_average, 2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ") ")
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ") ")
