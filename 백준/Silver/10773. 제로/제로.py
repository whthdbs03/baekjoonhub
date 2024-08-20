a= int(input())
x=[]
s=0
for i in range(a):
    t=int(input())
    if t!=0:
        x.append(t)
    else:
        x.pop()
for i in range(len(x)):
    s+=x[i]
print(s)