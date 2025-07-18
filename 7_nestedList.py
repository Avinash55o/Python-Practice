n= int(input("no of students: "))
final_list=[]
score_list=[]
name_list=[]
# for loop to make a nested list that we want
for i in range(n):    
        l=[]
        name = input("give the name:")
        score = float(input("give the score: "))
        l.append(name)
        l.append(score)
        print(l)
        z=final_list.append(l)
        print(final_list)
# MAIN LOGIC PART

# Make a new score list to only store the scores
for i in range(len(final_list)):
        score_list.append(final_list[i][1])

# To get the lowest no--- return the value
lowest_score= min(score_list)

# to remove all the lowest scores if there are
for i in range(len(score_list)):
        if score_list[i] == lowest_score:
                score_list.remove()

# from the list that we have remove all the lowest no we can get the second lowest scores
second_lowest=min(score_list)
#  we need to find the names that got the second lowest marks: so we will compare all the socres in the final list that is equal to the second lowest and stor them in the empty name list
for i in range(len(final_list)):
        if second_lowest == final_list[i][1]:
                name_list.append(final_list[i][0])

# to make the names in alphabatical order
name_list.sort()

for i in name_list:
        print(i)
