x=int(input("enter the number"))
f1=0
f2=1
for i in range(x):
    print(f1)
    temp=f1
    f1=f2
    f2=temp+f2
    print("done")