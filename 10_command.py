N = int(input("give the no of commands:")) # no of commands like 4,5
my_list=[]
final_list=[]   
for i in range(N):
        command= input("give the command:") # if the command is like remove 3 
        my_list.append(command) # "remove 3" will append as a string
        
    # final out put in my_list= ["remove 3","insert 2 3"]

#WE NEED TO ITERATE N  NO OF TIME SO IT RUN HOW MANY COMMANDS WE HAVE 
for i in range(N):
        # NOW THE FIRST ELEMENT WILL SPLIT eg: "remove 3" ---> ["remove", "3"]
        split_list=my_list[i].split() 

        # every time the command will be in the 0th position     
        match split_list[0]:
            case "insert":
                # insert takes int value as a parameter 
                final_list.insert(int(split_list[1]),int(split_list[2]))
            case "print":
                print(final_list)
            case "remove":
                # remove also take int as a parameter 
                final_list.remove(int(split_list[1]))
            case "append":
                # same for the append 
                final_list.append(int(split_list[1]))
            case "sort":
                final_list.sort()
            case "pop":
                # pop default take -1 as a value and pop the last element 
                final_list.pop()
            case "reverse":
                final_list.reverse()