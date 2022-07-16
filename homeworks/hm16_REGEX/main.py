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
email_pattern = r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
email_text = input("\n2. Search for an email in text. \n Input your text: ")

regex2 = re.fullmatch(pattern=email_pattern, string=email_text)
if not regex2:
    print("2. Email not found")
else:
    print("2. Email is: ", regex2.group())

#  3. Write a Python program to remove redundant zeros from an IP address.
ip_text_with_zero = input("\n3. Input your ip: ")

ip_pattern = r"([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])[.]([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])[.]" \
             r"([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])[.]([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])"

regex3 = re.findall(pattern=ip_pattern, string=ip_text_with_zero)
if not regex3:
    print("4. IP number not found")
else:
    myRegex = ', '.join('.'.join(tup) for tup in regex3)
    regex_ip = re.sub(r'\b0+(\d)', r'\1', myRegex)
    print(f"\n3. {regex_ip}")


# 4. Write a Python program that check if IP address is valid.
ip_pattern = r"([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])[.]([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])[.]" \
             r"([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])[.]([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])"
ip_text = input("\n4. Input your IP: ")

regex4 = re.findall(pattern=ip_pattern, string=ip_text)
if not regex4:
    print("4. IP number not found")
else:
    myRegex = ', '.join('.'.join(tup) for tup in regex4)
    print(f"4. IP number is: {myRegex}")
