s1 = {1,2,3,4,5}
print(s1)

s2={"a","b","a","c","d"}
print(s2)

s1.add(6)
print(s1)

s1.remove(3)
print(s1)
s1.discard(2)
print(s1)

s3= {20,30,40}
s4={30,40,50,60}
print(s3|s4)
print(s3 & s4 )

print(s1-s2)
print(s1.issubset(s2))

s5= {20,30,40,50,60}
print(s5.issuperset(s3))

print(s1.isdisjoint(s2))

for num in s1:
    print(num)
