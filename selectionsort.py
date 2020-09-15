num=eval(input("enter number of elements"))
a=[]
for i in range(0,num):
    b=int(input("enter number of elements"))
    a.append(b)
for i in range(len(a)):
    mini=i
    for j in range(i+1,len(a)):
        if(a[mini]>a[j]):
            mini=j
    a[mini],a[i]=a[i],a[mini]
print("sorted list is")
for i in range(len(a)):
             print(a[i])
               

