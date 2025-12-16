str=input('Enter a string:')
word=str.split()
words=[i for i in word if len(i)<5]
print(words)