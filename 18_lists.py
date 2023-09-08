l=[3,5,6,'harry',True] #Lists are ordered collection of data items are alterable
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])
print(l[-4])
if 7 in l:
    print('Yes')
else:
    print("No")
# same thing applies for Strings as Well !
#if 'ha' in "harry":
#   print("Yes")
print(l[1:-1]) #1:4
print(l[1:-1:2]) #1:4:2 -jump index which jumps the number od items mentioned
lst=[i*i for i in range(10)if i%2==0]  # list comprehension
print(lst)