import re

# 1. Write a Python program which search a phone numbers.
phone_pattern = r"\d{3}[-]\d{2}[-]\d{2}"
phone_text = input("1. Search for a phone number in text. \n Input your text: ")

regex = re.findall(pattern=phone_pattern, string=phone_text)
if not regex:
    print("1. Phone number not found")
else:
    myRegex = ', '.join(regex)
    print(f"1. Phone number is: {myRegex}")

# 2. Write a validation for email following all the rules.
email_pattern = r"([\w+[._-])*[\w]+@[\w+[._-]+(\.[A-Z|a-z]{2,})+"
email_text = input("\n2. Search for an email in text. \n Input your text: ")

regex2 = re.fullmatch(pattern=email_pattern, string=email_text)
if not regex2:
    print("2. Email not found")
else:
    print("2. Email is: ", regex2.group())

#  3. Write a Python program to remove redundant zeros from an IP address.
ip_text_with_zero = input("\n3. Input your ip: ")

regex_pattern = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

if re.search(regex_pattern, ip_text_with_zero):
    regex3 = re.findall(pattern=regex_pattern, string=ip_text_with_zero)
    regex3_1 = ', '.join('.'.join(tup) for tup in regex3)
    regex3_2 = re.sub(r'\b0+(\d)', r'\1', regex3_1)
    print(f"\n ip: {regex3_2}")
else:
    print(f"{ip_text_with_zero} is an invalid IP address.")

# 4. Write a Python program that check if IP address is valid.
regex4 = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

ip_text = input("\n4. Input your IP: ")

if re.search(regex4, ip_text):
    print(f"{ip_text} is a valid IP address.")
else:
    print(f"{ip_text} is an invalid IP address.")
