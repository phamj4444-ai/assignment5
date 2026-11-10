#Write a function that will determine the frequency of a word (i.e. 
# how many times does a word appears) in a given piece of text
# . Hint: Use the dictionary data structure.
def read_word():
    text = input("enter the text:")
    words= text.split()
    count={}
    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1
    return count

print(
read_word())

