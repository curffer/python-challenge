import os
import csv
csvpath = os.path.join('..','PyBank/Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    months=0
    netTotal=0
    lastProfit=1088983
    greatestProfit=0
    greatestLoss=0
    totalChange=0
    for row in csvreader:
        profit=int(row[1])
        change=profit-lastProfit
        totalChange=totalChange+change
        months=months+1
        netTotal=netTotal + profit
        lastProfit=profit
        if profit > greatestProfit:
            greatestProfit=profit
            greatestProfitDate=row[0]
        if profit < greatestLoss:
            greatestLoss=profit
            greatestLossDate=row[0]
averageChange=round(totalChange/months,2)
output="Financial Analysis\n----------------\nTotal Months: "+str(months)+"\nTotal: $"+str(netTotal)+"\nAverage Change: $"+str(averageChange)+"\nGreatest Increase in Profit: "+greatestProfitDate+"($"+str(greatestProfit)+")\nGreatest Decrease in Profit: "+greatestLossDate+"($"+str(greatestLoss)+")"
print(output)
output_path = os.path.join("..", "PyBank/analysis", "results.txt")
with open(output_path, "w") as f:
    f.write(output)
