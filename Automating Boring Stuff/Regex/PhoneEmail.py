#Project: Phone Number and Email Address Extractor
#Use the pyperclip module to copy and paste strings.
#Create two regexes, one for matching phone numbers and the other for matching email addresses.
#Find all matches, not just the first match, of both regexes.
#Neatly format the matched strings into a single string to paste.
#Display some kind of message if no matches were found in the text.
import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

#Create email regex
emailRegex = re.compile(r'''(
   [a-zA-Z0-9._%+-]+      # username
   @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
     (\.[a-zA-Z]{2,4})       # dot-something
    )''', re.VERBOSE)

#Find matches in clipboard text
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])
# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
    
#Running the Program
#For an example, open your web browser to the No Starch Press contact page at https://nostarch.com/contactus/,
#press CTRL-A to select all the text on the page, and press CTRL-C to copy it to the clipboard. 