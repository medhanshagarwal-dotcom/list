l=[1,2,3,232, 7,332 ,5 ,7,3, 1101010,7]
print("original list = ", l)
c=0
for i in l :
    c+=i

avg=c/len(l)
print("sum of all number is: ", c)
print("the average of all numbers is: ", avg)

l.sort()

print("smallest element = " ,l[0])
print("largest element = ", l[-1])
print(l)