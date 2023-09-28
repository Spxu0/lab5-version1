# Q5.	Use the json module to read the course_info.json file from the previous question.
#  Display the course name and the average grade for the course. 
# The output should be as follows.
# Course Name                  Average Grade
# Advanced Programming                 81.8 

from statistics import mean
import json
with open ('course_info.json','r') as co:
    course=json.load(co)
    print(f'Course Name {"Average Grade":>18}\n{course["course_name"]}{mean(course["grades"]):>10}')

