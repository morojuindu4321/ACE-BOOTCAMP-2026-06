from functools import reduce
slist=[1,2,3,4,5,6,7,8,9,10]
print((reduce(lambda x,y:x+y, slist)))
print((reduce(lambda x,y:x*y, slist)))
xlist=[["xyz",1],["pqr",3],["klm",2],["abc",4]]
print(list(sorted(xlist,key=lambda x: x[0])))
print(list(sorted(xlist,key=lambda x: x[1])))



