# Q1.	Given the following dictionary temperatures, 

# which contains Celsius temperatures samples for three days.
temperatures = { 'Monday': '45, 45, 42, 39',
                 'Tuesday': '42, 42, 40, 41',
                 'Wednesday':'31, 32, 41, 45'}

# Write a Python code that stores temperature information into temperature.txt plain text file. Each record represents a day and its related temperature samples. The output should be formatted as follows.
# Monday 45 45 42 39
# Tuesday 42 42 40 41
# Wednesday 31 32 41 45


with open ('temperature.txt','w') as temp:
    for day in temperatures:
        temp.write(f'{day} {temperatures[day].replace(",","")}\n')