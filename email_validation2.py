#email validation using RegEx
import re
email_criteria="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("enter your email: ")
if re.search(email_criteria,user_email):
    print("valid input")
else:
    print("invalid input")

