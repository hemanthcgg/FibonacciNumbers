def Fibonacci(n):
    res=[]
    if(n==1):
        return(res.append(0)) 
    if(n==2):
        res.append(0)
        return(res.append(1)) 
    res=[0,1]
    a,b=0,1
    for i in range(3,n+1):
        c=a+b
        res.append(c)
        a=b
        b=c
    return res

n=int(input("Enter no.of numbers to be in sequence: ")) #Enter The Size of Sequence
print(*Fibonacci(n))  #Function call to print the Fibonacci Numbers upto Sequence of "n" Number 