#open and read
file=open("notes.txt","r")
print(file.read())
file.close()

#with context manager
with open("notes.txt","r")as file:
    print(file.read())

#reading text files
with open("notes.txt","r")as file:
    data=file.read()
print(data)

#write
with open("notes.txt","w")as file:
    file.write("hello")

#append
with open("notes.txt", "a") as file:
    file.write("\ntoday i learned Append Mode.")
print("Data added successfully!")

#csv module
import csv
with open("student.csv","w",newline="")as file:
    writer=csv.writer(file)
    writer.writerow(["Name","Age"])
    writer.writerow(["Ram",21])

#reading csv 
import csv
with open("student.csv","r")as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

#json module
import json
students={
    "name":"aaryan",
    "marks":95,
    "branch":"AIML"
}
with open("students.json","w")as file:
    json.dump(students,file)

#reading json
import json
with open("students.json","r")as file:
    data=json.load(file)
print(data)
print(data["marks"])

#read binary
with open("pin.jpg", "rb") as file:
    data = file.read()
print(data[:50])

"""if tried with r instead of rb we get an error like UnicodeDecodeError """
