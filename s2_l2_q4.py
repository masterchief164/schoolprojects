# use pip install stdiomask before executing
# question 4
import stdiomask
from string import punctuation


def checkUsername(username):
    exUsername = ["xyz_23", "abc-123", "lmn_5", "email.id.is", "whats_up"]
    special = False
    whitespace = False
    existing = False
    length = False
    first = username[0].isalpha()
    for i in username:
        if i == ' ':
            whitespace = True
        if i == '.' or i == '_' or i == '-':
            special = True
    if username in exUsername:
        existing = True
    if len(username) < 100:
        length = True
    if special and not whitespace and not existing and length and first:
        return True
    else:
        return False


def checkPass(passwd):
    symbols = list(punctuation)
    special = False
    length = False
    uppercase = False
    lowercase = False
    digit = False
    if 7 < len(passwd) < 100:
        length = True
    for i in passwd:
        if i in symbols:
            special = True
        if i.isupper():
            uppercase = True
        if i.islower():
            lowercase = True
        if i.isdigit():
            digit = True
    if length and uppercase and lowercase and digit and special:
        return True
    else:
        return False


username = input("Username: ")
passwd = stdiomask.getpass(mask='*')
while not (checkUsername(username) or checkPass(passwd)):
    if not (checkUsername(username)):
        print("Invalid Username")
    if not (checkPass(passwd)):
        print("Invalid Password")
    username = input("Username: ")
    passwd = stdiomask.getpass(prompt="Password: ", mask='*')

print("Valid id and password: Accepted")
