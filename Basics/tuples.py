colors=("red","blue","green","yellow","red","green")
print(colors)
print(len(colors))

print(colors[0])
print(colors[-1])

print(colors[1:])

#built-in methods 
print(colors.count("red"))
print(colors.index("green"))

#loops
for color in colors:
    print(color,end=" ")

#packing and unpacking

student= ("sania",21,"java")
name,age,course = student

print(name,age,course)


tup=("Hello",3.6,4,True,[1,2,3],{"fruits":"Apple"})
print(tup)

opertions: slicing
print(tup[0:4])
print(tup[::-1])
print(tup[1])

#concatenation 
numbers= (1,2,3,4,5)
total = colors +tup + numbers
print(total)

nums=[("a",1), ("b",2),("c",3)]
out= dict(nums)
print(out)


a=tuple(map(lambda x: x * x, [1, 2, 3]))
print(a)# returns a tuple

b= tuple(x for x in range(5))
print(b)

num= (20,59,34)
print(num)
del num
print(num)