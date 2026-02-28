a=[1,2,2,3,4,4,5]
for i in a:
    if a.count(i)>1:
        a.remove(i)
print(a)
