# hackerrank challenge
# https://www.hackerrank.com/challenges/tuple/hash/problem
# Given an integer n and n space-separated integers, create a tuple of those integers and print its hash.

#takes the input
n=int(input())
# takes the space-separated integers
seperated_int= input()
# so i convert the string to list of integers
# map function is used to apply int to each element of the list
# also can use chnged_list=tuple(map(int, seperated_int.split()))
chnged_list=list(map(int,seperated_int.split()))
# convert the list to tuple
t=tuple(chnged_list)
# print the hash of the tuple
print(hash(t))