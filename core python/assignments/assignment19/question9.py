def palindrome_num():
    n=0
    
    while(True):
        temp=n
        rev=0
        while(temp>0):
            digit=temp%10
            rev=rev*10+digit
            temp=temp//10
        if(rev==n):
            yield n
        n+=1
res=palindrome_num()
for i in range(1,30):
    print(next(res))