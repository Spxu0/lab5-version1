# Q6.Reimplement Q1 using the csv module to write the temperature information to a file,
#  named temperature.csv, in CSV format.

temperatures = { 'Monday': '45, 45, 42, 39',
                 'Tuesday': '42, 42, 40, 41',
                 'Wednesday':'31, 32, 41, 45'}


# for x in temperatures:
    
#     string=temperatures[x].replace(',','').split()

import csv 

with open('temperature.csv','w',newline='') as temp:
    write=csv.writer(temp)
    for x in temperatures:
        string=temperatures[x].replace(',','').split()
        
        string.insert(0,x)
        write.writerow(string)