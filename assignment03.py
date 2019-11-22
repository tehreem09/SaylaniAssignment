# question01
val1 = input("Enter first number > ")
operator = input("Enter operation to be applied (from + - * / e) > ")
val2 = input("Enter second number > ")
if operator == 'e': operator = '**'
result = eval(val1+operator+val2)
print("Resultant value > ", result)

# question02
list1 = [2.5, 'banana', 'x', True, 55, 'mango', 100, False, 'invalid']
print('\nList > ', list1)
list1 = [x for x in list1 if isinstance(x, (int,float))]
if not list1: print("[+] There is no numeric value in the list.")
else: print("[+] Numeric value is present in the list.")

# question03
my_dict = {'a': 'abc', 'b': 'bcd', 'c': 'cde', 'd': 'def'}
key = input('\nEnter key to be added > ')
my_dict.update({key: None})
print(my_dict)

# question04
my_dict = {'a': 1, 'b': 3, 'c': 10, 'd': 5}
sum_result = sum(my_dict.values())
print('\nDictionary > ', my_dict)
print('[+] Sum of numeric values in dictionary > ', sum_result)

# question05
list1 = [2, 4, 9, 7, 2, 5, 7, 9, 10]
x=set(list1)
dup=[]
print('\n', list1)
for c in x:
    if list1.count(c)>1:
        dup.append(c)
if not dup:print('[+] No duplicates found.')
else:print('[+] Duplicate values > ', dup)

# question06
key = input('\nEnter key to check > ')
if key in my_dict: print('[+] Key found.')
else: print('[+] Key not found.')