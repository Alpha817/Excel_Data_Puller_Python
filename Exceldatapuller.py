import pandas as pd
ex_file = pd.read_excel("PATH TO FILE")
students = ex_file.get("students")
u_input = input("Enter space separated list of student then test to search, EG: nate test1") #You'll have to probably rename the colum headers in the excel sheet so there' no spaces between test and #
u_input = u_input.split()
student_index = list(students).index(u_input[0])
test_score = list(ex_file.get(u_input[1]))[student_index]
print(f"Student {u_input[0]}'s score for {u_input[0]} is {test_score}")
   