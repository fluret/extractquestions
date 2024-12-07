import re

def check_password_validity(password):
    if (6 <= len(password) <= 12 and
        re.search("[a-z]", password) and
        re.search("[0-9]", password) and
        re.search("[A-Z]", password) and
        re.search("[$#@]", password) and
        not re.search("\s", password)):
        return True
    return False

input_passwords = input("Entrez une séquence de mots de passe séparés par des virgules : ")
passwords = input_passwords.split(',')

valid_passwords = [password for password in passwords if check_password_validity(password)]

print(",".join(valid_passwords))