import os
import csv

# specify path of text file and specify path of analysis file for output 
os.chdir(os.path.dirname(os.path.abspath(__file__)))
budget_data = os.path.join("Resources","budget_data.csv")



# read text file
with open(budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

months=0
total=0
average_change=0
Geatest_increase=0
Greates_decrease=0

profitandloss=[]
all_csv=[]
totals = []
with open(budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        months+=1
        total+=int(row[1])
        profitandloss.append(int(row[1]))
        all_csv.append([row[0], int(row[1])])
        totals.append(total)
        
       
sum=0
changes=[]

length = len(profitandloss)-1
for i in range(0,length):
    changes.append(profitandloss[i+1]- profitandloss[i])
    sum = sum + changes[i]
ave_change=sum/total
gre_inc=max(changes)
gre_inc_ind=changes.index(max(changes))+1
gre_dec=min(changes)
gre_dec_ind=changes.index(min(changes))+1


print(f"\nFinancial Analysis\n")
print(f"----------------------------------------\n")
print(f"Total months: {months}\n")
print(f"Total: ${total}\n")
print(f"Average  Change: ${round(average_change, 2)}\n")
print(f"Greatest Increase in Profits: {all_csv[gre_inc_ind][0]}, (${gre_inc})\n")
print(f"Greatest Decrease in Profits: {all_csv[gre_dec_ind][0]}, (${gre_dec})\n")




with open(output_path, "w") as txt_file:
    txt_file.write(output)