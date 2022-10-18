import os
import csv
csvpath = os.path.join('..','PyPoll/Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    candidates=[]
    dict=[]
    percents=[]
    totalVotes=0
    for row in csvreader:
        totalVotes=totalVotes+1
        if row[2] not in candidates:
            candidates.append(row[2])
            dict.append({"name":row[2],"votes":1,"percent":0})
        else:
            index=candidates.index(row[2])
            dict[index]["votes"]=dict[index]["votes"]+1
output_path = os.path.join("..", "PyPoll/analysis", "results.txt")
highestVotes=0
name=""
for name in candidates:
    index=candidates.index(name)
    dict[index]["percent"]=dict[index]["votes"]/totalVotes*100
    if dict[index]["votes"]>highestVotes:
        highestVotes=dict[index]["votes"]
        winner=dict[index]["name"]
with open(output_path, "w") as f:
    f.write("Election Results\n---------------\nTotal Votes: "+str(totalVotes)+"\n------------------")
    for name in candidates:
        index=candidates.index(name)
        f.write("\n"+name+": "+str(round(dict[index]["percent"],2))+"% ("+str(dict[index]["votes"])+")")
    f.write("\n-----------------\nWinner: "+ winner+"\n-------------")
print("Election Results\n---------------\nTotal Votes: "+str(totalVotes)+"\n------------------")
for name in candidates:
    index=candidates.index(name)
    print("\n"+name+": "+str(round(dict[index]["percent"],2))+"% ("+str(dict[index]["votes"])+")")
print("\n-----------------\nWinner: "+ winner+"\n-------------")

