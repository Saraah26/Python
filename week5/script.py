with open("setup.txt","w") as file:
    file.write("Python Created a new file")

text_data = """ Name, Age, Location
Alice, 22, England
Bob, 20, Paris
Carol, 23, London"""

with open("data.csv","w") as file:
    file.write(text_data)
print("python file successfully created!")

plain_text = """Line 1 = Hello this is a setup text file
line 2 = Python makes it easy to manage files
Line 3 = this is the last line of this file"""

with open("setup.txt","w") as file:
    file.write(plain_text)
print("File 'setup.txt' updated successfully")

#read mode
with open("setup.txt","r") as file:
    content = file.read()
    print(content)

#read line by line
with open("setup.txt","r") as file:
    for line in file:
        print(line.strip())

#appending 
with open("data.csv","a") as file:
    file.write("this line is appended at the end of file.")

text_lines = ["Line 1 = Hello this is a setup text file \n"
"Line 2 = Python makes it easy to manage files\n"
"Line 3 = this is the last line of this file\n"]

with open("setup.txt","w") as file:
    file.writelines(text_lines)
print("File 'setup.txt' has updated successfully")

with open("log.txt","w") as file:
    file.write("Initialized successfully!")

with open("log.txt","a") as file:
    file.write("This line is appended successfully!\n")


