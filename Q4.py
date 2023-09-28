# Q4.	Use the json module to write the following course information to a file,
#  in JSON format. Name the file course_info.json
course = {'course_name':'Advanced Programming',
          'grades': [86, 90, 96, 64, 73],
          'year': '2021'}

import json
with open ('course_info.json','w',newline="") as co:
    json.dump(course,co)
    

