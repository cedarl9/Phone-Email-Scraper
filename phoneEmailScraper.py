#! python3
#TODO:
#create regex for phone
#create regex for email
#import text
#extract from text
#paste to clipboard
#types of nums we accept: 1111-222-3333,111-2222, (111) 222-3333, 111-2222 ext 12345, ext. 12345, x12345

import pyperclip, re

#phone regex. verbose and ''' lets me use #
phoneRegex = re.compile(r'''
(((\(\d\d\d\)) |      #(---)
(\d\d\d))?          #--- set to appear 0 or 1 times with ?
(\s|-)                #first seperator
\d\d\d                #first 3 digits
-                     #2nd sep
\d\d\d\d            #last 4 digits
((ext(\.)?\s |x)        #ext. or ext or x
(\d{2, 5}))?)       #extension number
''', re.VERBOSE)

#email regex
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+    # name
@                    #@
[a-zA-Z0-9_.+]+      #domain
''', re.VERBOSE)

#get text off clipboard
text = pyperclip.paste()

#extract phoone / email
extractedPhone = phoneRegex.findall(text) #returns tuples
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone: #gets the number from the tuple
    allPhoneNumbers.append(phoneNumber[0]) #tuple 0 because we put () around the whole regex

#join nums, emails each on a new line
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)

pyperclip.copy(results)
print("This is the phone number list then the email list. It is also in your clipboard.")
print(results)