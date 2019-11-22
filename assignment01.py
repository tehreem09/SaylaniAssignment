import sys
import datetime
import math

# question01
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")

# question02
print("\n[+] Python version > " + sys.version)

# question03
print("\n[+] Current date and time >", datetime.datetime.now())

# question04
radius = float(input("\nEnter Radius > "))
area = math.pi * radius**2
print("[+] Area of the circle >", area)

# question05
first_name = input("\nEnter your first name > ")
last_name = input("Enter your last name > ")
print("[+] Your name in reverse order > "+last_name,first_name)

# question06
value1 = float(input("\nEnter first value > "))
value2 = float(input("Enter second value > "))
print("[+] Addition of both values > ", value1+value2)