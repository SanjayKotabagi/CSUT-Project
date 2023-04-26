import string
import requests
import random as r
import re


def getmailinfo(mail):
    endpoint = f"https://emailrep.io/{mail}"
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        # Get results
        results = response.json()
        
        return results['details']
        # print(results)
    else:
        # print("Failed")
        return response.status_code

# print(getmailinfo('sanjaymkotabagi@gmail.com'))


def genpassword(l):
    characters = string.ascii_letters + string.digits + string.punctuation
    shuffled_characters = r.sample(characters, l)
    # Generate the password
    password = ''.join(shuffled_characters)
    return password

# print(genpassword(15))

def checkpassword(password):
    upper_pattern = re.compile(r'[A-Z]')

    # Define the pattern to check for lowercase letters
    lower_pattern = re.compile(r'[a-z]')

    # Define the pattern to check for digits
    digit_pattern = re.compile(r'\d')

    # Define the pattern to check for symbols
    symbol_pattern = re.compile(r'[^\w\s]')

    # Check the password against the patterns
    if len(password) < 8:
        return "Password is too short"
    elif not upper_pattern.search(password):
        return "Password should contain at least one uppercase letter"
    elif not lower_pattern.search(password):
        return "Password should contain at least one lowercase letter"
    elif not digit_pattern.search(password):
        return "Password should contain at least one digit"
    elif not symbol_pattern.search(password):
        return "Password should contain at least one symbol"
    else:
        return "Password is strong"

# print(checkpassword('Sjmfeo@dsfsdf'))