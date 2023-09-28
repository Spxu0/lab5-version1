# Q2.	Write a Python code that appends a new record to the temperature.txt file  
# you created in the previous question. The records contains 
# the following temperature samples for Friday: 31, 32, 41 and 45.
# Monday 45 45 42 39
# Tuesday 42 42 40 41
# Wednesday 31 32 41 45
# Friday 31 32 41 45


with open ('temperature.txt','a') as temp:
    temp.write("Friday 31 32 41 45")