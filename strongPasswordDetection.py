import re

# create password regex for upper and lower case and digits
passwordRegex1 = re.compile(r'[a-zA-Z0-9]')

# create password regex for minimum 8 characters length
passwordRegex2 = re.compile(r'(\w{8})')

# function to check if a password is strong
def isStrongPassword(s) -> bool:
    strongPassword = ''
    if (strongPassword == passwordRegex1.findall(s)) | (strongPassword >= passwordRegex2.findall(s)):
        return True
    return False
    

isStrongPassword('fable')