#  It must have the username@websitename.extension format type.
#  The username can only contain letters, digits, dashes and underscores.
#  The website name can only have letters and digits.
#  The maximum length of the extension is 3
import re

# sample_email = 'whatever@google.com'

def whatever(s):
    match = re.match('^(\w|\d|\-|\_)+\@([A-Za-z]|\d)+\.\w{1,3}$',s)

    if match:
        print True
        print match.group()
    else:
        print False

sampleList = ['its@gmail.com1','mike13445@yahoomail9.server','rase23@ha_ch.com',\
              'daniyal@gmail.coma','thatisit@thatisit']

for email in sampleList:
    whatever(email)
