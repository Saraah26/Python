#reading fom CSV files
import csv
with open("data.csv","r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
# writing form CSV files
import csv
Data = [
    ["Name","Age","Role"],
    ["Albert","21","Intern"],
    ["Bob","23","Data Analyst"]
]
with open("output.csv","w") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(Data)

#reading a json file
#creating a json file

import json

# STEP 1: Create the 'user.json' file first so it exists!
user_profile = {
    "Name": "Albert",
    "Age": 21,
    "Role": "Intern"
}

with open("user.json", "w") as file:
    json.dump(user_profile, file, indent=4)

print("--- user.json created successfully! ---")

with open("user.json", "r") as file:
    user_data = json.load(file)

print(user_data)
print(user_data["Name"])

import json

user_profile = {"Name": "Albert", "Age": 21}
with open("user.json", "w") as file:
    json.dump(user_profile, file) 
    
import json

with open("user.json", "r") as file:
    user_data = json.load(file)

print(user_data["Name"])  