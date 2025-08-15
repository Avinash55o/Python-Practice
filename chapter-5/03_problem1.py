words={
    "garv":"proud",
    "khushi":"happiness",
    "sukh":"peace",
}

input_word=input("enter the hindi word:")

print(words.get(input_word))  # prints the meaning of the word
# a little different between up and down
print(words[input_word])  # also prints the meaning of the word, but will raise KeyError if the key does not exist