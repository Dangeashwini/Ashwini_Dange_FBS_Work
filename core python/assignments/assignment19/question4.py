str=input("Enter a string:")
new_str=''.join([i for i in str if i not in 'aeiou'])
print(new_str)