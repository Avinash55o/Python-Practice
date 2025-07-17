# QUESTION ---> Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.



n = int(input("no of participent"))
arr = map(int, input("give the score list:").split()) #map funtion -- map(function, iterables)
score_list= list(arr)
print("the score list", score_list)
max_no= max(score_list)
print("the max no is",max_no)
s=[]

# in this for loop i think that i that i useing is index in this insted i should be using the val
"""for i in range(0,len(score_list)):
   if i < max_no:
        s.append(i)
    else:
        print("kam nhi kia")
"""
# new for loop
for val in score_list:
    if val < max_no:
        s.append(val)
    else:
        print("nhi hoga")
       
print(s)          
second=max(s)
print(second)



