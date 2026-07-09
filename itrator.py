my_list= ["apple","Mamgo","cherry","orange"]
my_iterator = iter(my_list)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

for index, fruit in enumerate(my_list):
    print(f"index {index}: {fruit}")

iterator_obj = ["Python", "java","c","c++"]

while True:
    try:
        items = next(iterator_obj)
        print(items)
    except StopIteration:
        break

