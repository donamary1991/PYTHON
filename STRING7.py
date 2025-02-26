# valid PAN ID or not
import re
x=input("enter the valid PAN").upper()
result=re.compile("[A-Za-z]{5}\d{4}[A-Za-z]{1}")
if result.match(x):
    print("valid PAN")
else:
    print("invalid PAN")

