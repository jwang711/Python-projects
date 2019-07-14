import os
import csv

budget_data = os.path.join(".","Resources", "budget_data.csv")
print(os.getcwd())

with open(budget_data, newline="") as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first
    csv_header = next(csvfile)
    # skip header row
    print(f"Header: {csv_header}")

 # find net amount of profit and loss
    P = []
    months = []

    #read through each row of data after header
    for rows in csvreader:
        months.append(rows[0])
        P.append(int(rows[1]))
        
      
    # calculate total length of months
    Count_months = len(months)
    
    # calculate total revenue
    total_revenue = sum(P)
    
    # calculate revenue change
    revenue_change = []

    for x in range(1, len(P)):
        revenue_change.append((int(P[x]) - int(P[x-1])))
    
    total_revenue_change = sum(revenue_change)
    
    #calculate average change
    average_change = total_revenue_change/Count_months
   
    #The greatest increase in profits (date and amount) over the entire period
    max_profits = max(P)

    #The greatest decrease in losses (date and amount) over the entire period
    min_profits = min(P)
       
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(Count_months))
    print("Total: " + str(sum(P)))
    print("Average Revenue Change: " + str(average_change))

    for i in range(len(P)):
        if P[i] == max_profits:
            print("Greatest Increase in Profits:" + (months[i]) + " " + "$" + str(max_profits))
    
    for i in range(len(P)):
        if P[i] == min_profits:
            print("Greatest Decrease in Profits:" + (months[i]) + " " + "$" + str(min_profits))


    with open('financial_analysis.txt', 'w') as file:
        file.write("----------------------------------------------------------\n")
        file.write("  Financial Analysis"+ "\n")
        file.write("----------------------------------------------------------\n\n")
        file.write("    Total Months: " + str(Count_months) + "\n")
        file.write("    Total: " + "$" + str(sum(P)) +"\n")
        file.write("    Average Revenue Change: " + '$' + str(average_change) + "\n")
        file.write("    Greatest Increase in Profits: " + (months[i]) + " " + "$" + str(max_profits) + "\n")
        file.write("    Greatest Decrease in Profits: " + (months[i]) + " " + "$" + str(min_profits) + "\n")
        file.write("----------------------------------------------------------\n")           
