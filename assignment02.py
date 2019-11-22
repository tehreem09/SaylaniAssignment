# question01
marks = []
total_marks = 0
for x in range(5):
    marks.append(float(input("Enter marks > ")))
    # print(marks[x])
    if 0 <= marks[x] <= 100:
        total_marks += marks[x]
    else:
        print("[-] Marks should be out of 100.\nPlease try again.")
        x -= 1
percentage = total_marks / 500 * 100
if percentage >= 90: print("[+] Your grade is A+.")
elif percentage >= 80: print("[+] Your grade is A.")
elif percentage >= 70: print("[+] Your grade is B.")
elif percentage >= 60: print("[+] Your grade is C.")
elif percentage >= 50: print("[+] Your grade is D.")
else: print("[+] Your grade is F.")

# question02
number = int(input("\nEnter number > "))
if number%2 == 0: print("[+] Given number is Even.")
else: print("[+] Given number is Odd.")

# # question03
list1 = [4, 22, 44, 3, 65, 32, 77, 1, 15, 86, 5]
print("\n", list1)
print("[+] List length > ",len(list1))

# question04
print("\n[+] Sum of list's item > ", sum(list1))

# question05
print("\n[+] Largest Number > ",max(list1))

# question06
list2 = []
print("\n[+] Elements in the list that are less than 5 ",end='> ')
for x in list1:
    if x < 5: list2.append(x)
print(*list2,sep=', ')