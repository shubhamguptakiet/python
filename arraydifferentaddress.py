from  numpy import *
arr1=array([1,2,3,4,5])
arr2=arr1
arr1=arr2.view()
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))