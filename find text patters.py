import re
log_data= "User ID_4829 logged in at 10:00. User ID_9021 logged out at 11:00"
pattern = r"ID_\d{4}"
user_ids = re.findall(pattern,log_data) 
print(user_ids)

# match(), findall(), search()
import re
text  = "apple 50, banana 60, mango 40, apple 30"
match_result1 = re.match(r"apple",text)
print(match_result1)

match_result2= re.match(r"mango",text)
print(match_result2)

#search()
search_result1= re.search(r"apple",text)
print(search_result1)

search_result2= re.search(r"banana",text)
print(search_result2)

#findall()
findall_result1=re.findall(r"apple",text)
print(findall_result1)

findall_result2= re.findall(r"mango",text)
print(findall_result2)

#to find all the numbers in a set
findall_num = re.findall(r"\d+",text)
print(findall_num)

findall_num = re.findall(r"\d*",text)
print(findall_num)

findall_num = re.findall(r"\d?",text)
print(findall_num)

findall_num = re.findall(r"\d{3}",text)
print(findall_num)