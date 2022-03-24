import pyperclip, re

# create phone regular expression

phoneRegex = re.compile(r'''(
    (\d{3}?|\(\d{3}\)?) # optional area code with and without brackets
    (\s|-|\.)? # separator
    (\d{3}) # first 3 digits
    (\s|-|\.) # separator
    (\d{4}) # last four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # optional extension
    
)''', re.VERBOSE)

# create email regular expression

emailRegex = re.compile(r'''(
    (\w+ | \W+)
    @
    (\w+ | \W+)
    (\.)
    (\w+ | \W+)
    
)''', re.VERBOSE)


# find matches in clipboard text

text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])


# copy results to the clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
    
# Now go to a website or any text you want to get phone numbers and email extracted from
# Select the entire text/webpage - Ctrl+A / Cmnd+A
# Copy the text - Ctrl+C / Cmnd+C
# Run the program
# The program will output the results printing 'Copied to clipboard:'
# If nothing found the program will print: 'No phone numbers or email addresses found.'