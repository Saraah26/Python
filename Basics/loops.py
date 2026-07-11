# for loop
numbers = [1,2,3,4,5,6]
for num in numbers:
    print(num)

word = "coding"
for char in word:
    print(char)

for i in range(1,10):
    print(i)

for i in range(1,15,2):
   print(i,end=" ")

# Nested for loop
for j in range(1,6):
    for k in range(1,4):
        for m in range(1,3):
             print(j,k,m)
        
# while loop 
i = 0
while i<= 10:
    print(i)
    i+= 1

# countdown

count =5
while count>0:
    print(count)
    count-= 1
print("Hello")

# break statement - immediately terminates the loop 

#for loop with break statement
for i in range(1,11):
    if i == 8:
        break
    print(i)

# while loop with break statement
i =2
while i<=10:
    if i==9:
        break
    print(i)
    i+=1

# continue Statement - skips the current iteration and continues with the next iteration of the loop
for i in range(1,11):
    if i == 8:
        continue
    print(i)

# while loop

i=1
while i<10:
    if i == 5:
        i+= 1
        continue
    print(i)
    i+= 1

print("hello world")

num= 5
fact =1

for i in range(1,num+1):
    fact*=i
print(fact)

#while loop

i=1
fact = 1

while i <num+1:
    fact*= i
    i+= 1
print(fact)

#first multiple of 7
for i in range(1,50):
    if i%7==0:
        print(i)
        break


# first 10 mutliples of 7 using while loop
count = 10
i=1
while i<=100:
    if i%7==0:
        print(i)
        count+=1
        if count == 10:
            break
