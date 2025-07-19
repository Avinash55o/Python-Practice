# hackerrank question --- find the percentage
n= int(input("no of student:"))
student_marks={}
for i in range(n):
    # in this the name variable will get the first word enter by the user and rest of the words will be in the list
    name, *line= input("give the name of the student").split()
    # print(name)
    #  print(line)
    
    # create a list of all the scores
    scores= list(map(float, line))
     # put the scores in the dictionary and name as a key
    student_marks[name] = scores

# the name for which the average score need to find
query_name= input("need to find the average of:")
# take out the list of score useing the name 
mark_list=student_marks.get(query_name)
# take out the average
average_marks= sum(mark_list)/len(mark_list)
# to get the result as 23.00 
formated= f"{average_marks:.2f}"
print(formated) # will give the output--> 23.00