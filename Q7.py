# Q7.	Use the csv module to read the attached accounts.csv file. 
#Each line in the file represents a bank customer information: name and balances for three accounts.
#  Display the name and  the total balance for the customer accounts. 
# Also, display the total balance for all customers. The output should be formatted as follows.

# Name            Total
# Fahad             140
# Saleh             147
# Sami              135

# Total(all customers): 422

import csv

with open ('accounts.csv','r',newline="") as acc:
    reader=csv.reader(acc)
    for data in reader:
        name ,balance=data
        print(name,balance)

