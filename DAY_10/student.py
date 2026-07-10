# creating sdetails.csv
import csv
with open("sdetails.csv","w",newline="")as file:
    writer=csv.writer(file)
    writer.writerow(["Name","Age","Branch"])
    writer.writerow(["Usha", 21, "AI & ML"])
    writer.writerow(["Rahul", 22, "CSE"])
    writer.writerow(["Priya", 20, "ECE"])
print("Student details saved successfully!")

#reading
import csv
with open("sdetails.csv","r")as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
        