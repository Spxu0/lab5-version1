# Q3.	Write a Python code that updates an existing record in the temperature.txt file. 
# You need to replace Wednesday with Sunday.
# Monday 45 45 42 39
# Tuesday 42 42 40 41
# Sunday 31 32 41 45
# Friday 31 32 41 45
import os

temperature=open('temperature.txt','r')
temp_file=open('temp_file.txt','w')

with temperature ,temp_file:
    for file in temperature:
        if file.startswith('Wednesday'):
            temp_file.write(file.replace('Wednesday','Sunday'))
        else:
            temp_file.write(file)

os.remove('temperature.txt')
os.rename('temp_file.txt','temperature.txt')