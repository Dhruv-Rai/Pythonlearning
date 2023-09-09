l=[11,23,44,16,2]
l.append(7)
print(l)
print(l.count(11))
# l.sort()
l.sort(reverse=True)
print(l)
#m=l.copy()
#m[0]=0
l.insert(1,899)
print(l)
m=[900,1000,1100]
#l.extend(m)
k=l+m
print(k)