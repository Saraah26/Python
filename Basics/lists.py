lang = ["Python", "C++", "C", "Java"]
print(lang)
print(lang[1])
print(lang[0])
print(lang[-2])

nums = [1,2,3,4,5]
print(nums[1:4])
print(nums[-3:-1])

#reversing the list
print(nums[::-1])

print(len(nums))
nums[1]=7
print(nums)

nums.append(10)
print(nums)

nums.extend([11,12,13])
nums.remove(4)
print(nums)
print(nums.clear())
print(nums)

colors= ["red", "blue", "green", "yellow", "red"]
print(colors.index("blue"))
print(colors.count("red"))
colors.sort()
print(colors)
print(len(colors))
print("red" in colors)
print("orange" in colors)
colors.insert(3,"purple")
print(colors)

