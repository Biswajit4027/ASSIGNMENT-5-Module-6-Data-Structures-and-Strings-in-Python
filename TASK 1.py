'''
Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
'''
print("\n")
print("----------------CREATE A DICTIONARY-------------")
dictionery={}
while True:
        name = input("Enter students name (KEY): ")
        marks = int(input("Enter marks obtained (VALUE): "))
        dictionery.update({name:marks})
        con=input("Press any key to continue (q to quit) : ")
        if con.lower()=='q':
            print("\n\n")
            break
        else:
            continue

print("----------YOUR DICTIONARY----------\n")
print("STUDENT NAME\tMARKS OBTAINED")
print("===================================")
for key,value in dictionery.items():
      print(f"{key:15}:\t{value}")
print("\n")

while True:
    n=input("Enter the name of the student to know the marks obtained: ")
    if dictionery.get(n):
        print(f"Marks obtained by {n} is : ",dictionery.get(n))
    else:
        print("The student name is not in the database \n")
    b=input("Press any key to continue (q to quit) : ")
    if b.lower()=='q':
         break
    else:
        continue




