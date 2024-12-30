# Write a Python program to print "Hello, World!".
print("hello World!.")

# Write a program to get first name and last name from the user, concatenate the them by using string
# concatenation and print the full name. hint: use input() function to get the input from the user.
first_name = input("please Enter First Name")
last_name =input("please Enter last Name")
print(first_name+last_name)

#Create a simple calculator without using ChatGPT or Gemini.
print("1.add")
print("2.substract")
print("3.multiply")
print("4.divide")
print("5.Modulus")
print("6.Exponentiation")
print("7.Floor Division")
choice =input("please choice a operator  : ")
if choice == "1":
    first_number = int(input("please Enter first number  :  "))
    Second_number = int(input("please Enter Second number : "))
    print(f"the result is :{first_number + Second_number} ")
elif choice == "2":
    first_number = int(input("please Enter first number  :  "))
    Second_number = int(input("please Enter Second number : "))
    print(f"the result is :{first_number - Second_number} ")
elif choice == "3":
    first_number = int(input("please Enter first number  :  "))
    Second_number = int(input("please Enter Second number : "))
    print(f"the result is :{first_number * Second_number} ")
elif choice == "4":
    first_number = int(input("please Enter first number  :  "))
    Second_number = int(input("please Enter Second number : "))
    print(f"the result is :{first_number / Second_number} ")
elif choice == "5":
    first_number = int(input("please Enter first number  :  "))
    Second_number = int(input("please Enter Second number : "))
    print(f"the result is :{first_number % Second_number} ")
elif choice == "6":
    first_number = int(input("please Enter first number  :  "))
    Second_number = int(input("please Enter Second number : "))
    print(f"the result is :{first_number ** Second_number} ")
elif choice == "7":
    first_number = int(input("please Enter first number  :  "))
    Second_number = int(input("please Enter Second number : "))
    print(f"the result is :{first_number // Second_number} ")
else:
    print("InValid Choice! Try Again")


#  Write a python program which takes student name, roll number, class venue and class schedule from the user.
#  Draft a email message to send to the student using fstring and .format() method. Print the message.
student_name = input("Please Enter your Name  :")
roll_number = input("Enter your roll number  : ")
class_venue = "Your classes will be held in the Air University Main Auditorium "
class_schedule = "saturday at 2:00pm  to 6:00pm"
email_massage_fstring = f"""
Dear {student_name},

Thank you for registering in the Python Programming course in PIAIC. Your roll number is {roll_number}.
{class_venue} on {class_schedule}
"""
print(email_massage_fstring)