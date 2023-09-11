s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)
# union method returns a new set whereas the update add up item into the existing set
city={"Tokyo",'Berlin','Madrid','Delhi'}
city2={'Tokyo','Seoul','Kabul','Delhi'}
city3=city.intersection(city2)# Those values which are common
print(city3)
city4=city.symmetric_difference(city2)#Those value which are not common
print(city4)
city5=city.difference(city2)# print item that are present only in original set and not in both the set
print(city5)
print(city.isdisjoint(city2)) # No items in common
print(city.issuperset(city2)) # Same to Subset
city.add("Dubai")# Adds an element
print(city)
city.discard("Dubai") # Removes the Element(.remove shows an error whereas discard does not if element is not present)
# del city // deletes the set
# clear city // clears all the element inside the set
item=city.pop() # pop out an Element
print(city)
print(item)