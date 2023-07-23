def powerWithModules(a,b,c):
    a=a%c
    result=1
    for i in range(b):
        result=(result*a)%c
    return result

a=int(input())
b=int(input())
c=int(input())
print(powerWithModules(a,b,c))