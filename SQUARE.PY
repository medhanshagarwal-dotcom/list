one=[int(input("Enter a number for the end part of range: "))]
j=one[-1]
m=0
l=[]
for i in range (1, j+1):
    m=j*j
    l.append(m)
    j-=1
print(l)
for i in l:
    if i%2==0:
        print(i," = even")
    else:
        print(i, " = odd")