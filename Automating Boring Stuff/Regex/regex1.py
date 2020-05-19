import re
'''
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('Is 415-555-4242 a phone number?')
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
  chunk = message[i:i+12]
  if isPhoneNumber(chunk):
          print('Phone number found: ' + chunk)
print('Done')


phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())


phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')

print(mo.group(1))
print(mo.group(2))

print(mo.groups())

areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)



#To match parentheses.
#The \( and \) escape characters in the raw string passed to re.compile() will match actual parenthesis characters. 
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))


#Matching multiple groups with a pipe
#When both Batman and Tina Fey occur in the searched string, the first occurrence of matching text will be returned as the Match object.

heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

#You can also use the pipe to match one of several patterns as part of your regex. For example, say you wanted to match
#any of the strings 'Batman', 'Batmobile', 'Batcopter', and 'Batbat'. Since all these strings start with Bat,
#it would be nice if you could specify that prefix only once. This can be done with parentheses.
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

#Optional matching with a question mark
#The (wo)? part of the regular expression means that the pattern wo is an optional group. The regex will match
#text that has zero instances or one instance of wo in it. This is why the regex matches both 'Batwoman' and 'Batman'.
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())

mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())

#Matching Zero or More with the Star
#The * (called the star or asterisk) means “match zero or more”—the group that precedes the star
#can occur any number of times in the text. It can be completely absent or repeated over and over again.
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

#Matching One or More with the Plus
#While * means “match zero or more,” the + (or plus) means “match one or more.” Unlike the star, which
#does not require its group to appear in the matched string, the group preceding a plus must appear at least once.

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)

#Matching Specific Repetitions with Braces
#If you have a group that you want to repeat a specific number of times, follow the group in your regex with a
#number in braces. For example, the regex (Ha){3} will match the string 'HaHaHa', but it will not match 'HaHa',
#since the latter has only two repeats of the (Ha) group.

#Instead of one number, you can specify a range by writing a minimum, a comma, and a maximum in between the braces.
#For example, the regex (Ha){3,5} will match 'HaHaHa', 'HaHaHaHa', and 'HaHaHaHaHa'.

#You can also leave out the first or second number in the braces to leave the minimum or maximum unbounded. For example,
#(Ha){3,} will match three or more instances of the (Ha) group, while (Ha){,5} will match zero to five instances.

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())


mo2 = haRegex.search('Ha')
print(mo2 == None)

#Greedy and Non-greedy Matching
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

#The findall() Method
#In addition to the search() method, Regex objects also have a findall() method. While search()
#will return a Match object of the first matched text in the searched string, the findall() method
#will return the strings of every match in the searched string.
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')


#Shorthand character class
#\d - Any numeric digit from 0 to 9.
#\D-Any character that is not a numeric digit from 0 to 9.
#\w-Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
#\W-Any character that is not a letter, numeric digit, or the underscore character.
#\s-Any space, tab, or newline character. (Think of this as matching “space” characters.)
#\S-Any character that is not a space, tab, or newline.

#The regular expression \d+\s\w+ will match text that has one or more numeric digits (\d+), followed by a
#whitespace character (\s), followed by one or more letter/digit/underscore characters (\w+). The findall()
#method returns all matching strings of the regex pattern in a list.
xmasRegex = re.compile(r'\d+\s\w+')
xmasList = []
xmasList = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(xmasList)

#Making Your Own Character Classes
#There are times when you want to match a set of characters but the shorthand character classes
#(\d, \w, \s, and so on) are too broad. You can define your own character class using square brackets.
#For example, the character class [aeiouAEIOU] will match any vowel, both lowercase and uppercase.
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowels = []
vowels = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(vowels)

#You can also include ranges of letters or numbers by using a hyphen. For example, the character class [a-zA-Z0-9]
#will match all lowercase letters, uppercase letters, and numbers.
#Note that inside the square brackets, the normal regular expression symbols are not interpreted as such.
#This means you do not need to escape the ., *, ?, or () characters with a preceding backslash. For example,
#the character class [0-5.] will match digits 0 to 5 and a period. You do not need to write it as [0-5\.].
#By placing a caret character (^) just after the character class’s opening bracket, you can make a negative character class.
#A negative character class will match all the characters that are not in the character class.
consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonants = []
consonants = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(consonants)

#The Caret and Dollar Sign Characters
#You can also use the caret symbol (^) at the start of a regex to indicate that a match must occur at the beginning of
#the searched text. Likewise, you can put a dollar sign ($) at the end of the regex to indicate the string must end
#with this regex pattern. And you can use the ^ and $ together to indicate that the entire string must match the regex—that
#is, it’s not enough for a match to be made on some subset of the string.
beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello, world!')
print(beginsWithHello.search('He said hello.') == None)

endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
print(endsWithNumber.search('Your number is forty two.') == None)

#The r'^\d+$' regular expression string matches strings that both begin and end with one or more numeric characters.
wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')
print(wholeStringIsNum.search('12345xyz67890') == None)
print(wholeStringIsNum.search('12  34567890') == None)

#The Wildcard Character
#The . (or dot) character in a regular expression is called a wildcard and will match any character except for a newline.
atRegex = re.compile(r'.at')
atList = []
atList = atRegex.findall('The cat in the hat sat on the flat mat.')
print(atList)

#Matching Everything with Dot-Star
#Sometimes you will want to match everything and anything. For example, say you want to match the string 'First Name:',
#followed by any and all text, followed by 'Last Name:', and then followed by anything again. You can use the dot-star (.*)
#to stand in for that “anything.” Remember that the dot character means “any single character except the newline,” and
#the star character means “zero or more of the preceding character.”

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

#The dot-star uses greedy mode: It will always try to match as much text as possible. To match any and all text in a
#non-greedy fashion, use the dot, star, and question mark (.*?). Like with braces, the question mark tells Python to match in a non-greedy way.
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

#Matching Newlines with the Dot Character
#The dot-star will match everything except a newline. By passing re.DOTALL as the second argument to re.compile(),
#you can make the dot character match all characters, including the newline character.

noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

Review of Regex Symbols
This chapter covered a lot of notation, so here’s a quick review of what you learned about basic regular expression syntax:

The ? matches zero or one of the preceding group.
The * matches zero or more of the preceding group.
The + matches one or more of the preceding group.
The {n} matches exactly n of the preceding group.
The {n,} matches n or more of the preceding group.
The {,m} matches 0 to m of the preceding group.
The {n,m} matches at least n and at most m of the preceding group.
{n,m}? or *? or +? performs a non-greedy match of the preceding group.
^spam means the string must begin with spam.
spam$ means the string must end with spam.
The . matches any character, except newline characters.
\d, \w, and \s match a digit, word, or space character, respectively.
\D, \W, and \S match anything except a digit, word, or space character, respectively.
[abc] matches any character between the brackets (such as a, b, or c).
[^abc] matches any character that isn’t between the brackets.

#Case-Insensitive Matching
#To make your regex case-insensitive, you can pass re.IGNORECASE or re.I as a second argument to re.compile().
robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())

print(robocop.search('ROBOCOP protects the innocent.').group())

print(robocop.search('Al, why does your programming book talk about robocop so much?').group())

#Substituting Strings with the sub() Method
#Regular expressions can not only find text patterns but can also substitute new text in place of those patterns.
#The sub() method for Regex objects is passed two arguments. The first argument is a string to replace any matches.
#The second is the string for the regular expression. The sub() method returns a string with the substitutions applied.
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

#Sometimes you may need to use the matched text itself as part of the substitution. In the first argument to sub(),
#you can type \1, \2, \3, and so on, to mean “Enter the text of group 1, 2, 3, and so on, in the substitution.”
#For example, say you want to censor the names of the secret agents by showing just the first letters of their names.
#To do this, you could use the regex Agent (\w)\w* and pass r'\1****' as the first argument to sub(). The \1 in that
#string will be replaced by whatever text was matched by group 1—that is, the (\w) group of the regular expression.
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

#Managing Complex Regexes
#Regular expressions are fine if the text pattern you need to match is simple. But matching complicated text patterns
#might require long, convoluted regular expressions. You can mitigate this by telling the re.compile() function to ignore
#whitespace and comments inside the regular expression string. This “verbose mode” can be enabled by passing the variable
#re.VERBOSE as the second argument to re.compile().

#phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}
#(\s*(ext|x|ext.)\s*\d{2,5})?)')
#phoneRegex = re.compile(r'''(
#    (\d{3}|\(\d{3}\))?            # area code
#    (\s|-|\.)?                    # separator
#    \d{3}                         # first 3 digits
#    (\s|-|\.)                     # separator
#    \d{4}                         # last 4 digits
#    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
#    )''', re.VERBOSE)


#Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
#What if you want to use re.VERBOSE to write comments in your regular expression but also want to use re.IGNORECASE to
#ignore capitalization? Unfortunately, the re.compile() function takes only a single value as its second argument.
#You can get around this limitation by combining the re.IGNORECASE, re.DOTALL, and re.VERBOSE variables using the pipe
#character (|), which in this context is known as the bitwise or operator.
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

'''
