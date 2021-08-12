from datetime import date
import random
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
today = date.today()
year = today.year
month = today.month
day = today.day

def check_email(mail):
    if re.match(regex, mail):
        return True


def create_form():
    First = input("Enter Your First name:")
    Last = input("Enter Your Last name:")
    age = input("Enter Your Age:")
    gender = input("Enter Your Gender:M/F")
    phone_no = input("Enter your Mobile number:")
    email = input("Enter your email:")
    if check_email(email) == False:
        print("Enter valid Email Address")
    Address = input("Enter your Address:")
    city = input("Enter your city:")
    state = input("Enter your city:")
    pincode = input("Enter your pincode")
    id_ = str(year) + str(month) + str(day) + str('s') + str(random.sample([0,1,2,3,4,5,6,7,8,9], 3))

    dec = input("Submit/Cancel")

    if dec.capitalize() == "Submit":
        print("Your form is Submitted")
        return f"{id_},{First}, {Last}, {age}, {gender}, {phone_no},{email},{Address},{city},{state},{pincode},"
    else:
        print("Your form is not submitted")


print(create_form())