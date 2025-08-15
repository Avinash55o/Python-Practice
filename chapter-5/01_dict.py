marks={
    "avi":100,
    "bob":90,
    "carl":80,
    "dave":70,
}
print(marks)

# methods of dictionary
print(marks.keys()) # returns keys of the dictionary
print(marks.items()) #same as print give all the items in the dictionary
print(marks.values())  # returns values of the dictionary

marks.update({"carl":60})  # can update the dict or add new key-value pair
