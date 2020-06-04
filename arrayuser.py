from array import*
arr=array('i',[])
n=int(input("enter the size of array"))
for i in range(n):
    x=int(input("enter the next array"))
    arr.append(x)
print(arr)

c=0
vals=int(input("enter the search item"))
for e in arr:
    if vals==e:
        print(c)
        break
    k+=1