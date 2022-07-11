import re

# Write a Python program which search a phone numbers.
phone_pattern = r"\d{3}[-]\d{2}[-]\d{2}"
phone_text = input("Search for a phone number in text. \n Input your text: ")

regex = re.findall(pattern=phone_pattern, string=phone_text)
if not regex:
    print("Phone number not found")
else:
    myRegex = ''.join(regex)
    print(f"Phone number is: {myRegex}")

# Write a validation for email following all the rules.
email_pattern = r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
email_text = input("\nSearch for an email in text. \n Input your text: ")

regex2 = re.fullmatch(pattern=email_pattern, string=email_text)
if not regex2:
    print("Email not found")
else:
    print("Email is: ", regex2.group())

#  Write a Python program to remove redundant zeros from an IP address.
ip_text_with_zero = input("\nInput your ip: ")

regex3 = re.sub(r'[0]', '', ip_text_with_zero)
print(regex3)

# Write a Python program that check if IP address is valid.
ip_pattern = r"\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}"
ip_text = input("\nInput your IP: ")

regex4 = re.findall(pattern=ip_pattern, string=ip_text)
if not regex4:
    print("IP number not found")
else:
    myRegex = ''.join(regex4)
    print(f"IP number is: {myRegex}")
