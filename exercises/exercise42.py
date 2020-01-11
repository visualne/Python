# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.
import re

def fillLists(sample):
    lowerCaseList = []
    upperCaseList = []
    oddDigitsList = []
    evenDigitsList = []

    for char in sample:
        #  checking for lowerCaseLetter and putting it in list.
        lowerCaseLetter = re.match('[a-z]',char)
        upperCaseLetter = re.match('[A-Z]',char)
        oddDigits = re.match('[1,3,5,7,9]',char)
        evenDigits = re.match('[2,4,6,8]',char)
        if lowerCaseLetter:
            lowerCaseList.append(lowerCaseLetter.group())
        elif upperCaseLetter:
            upperCaseList.append(upperCaseLetter.group())
        elif oddDigits:
            oddDigitsList.append(oddDigits.group())
        else:
            evenDigitsList.append(evenDigits.group())


    return sorted(lowerCaseList) + sorted(upperCaseList)\
           + sorted(oddDigitsList) + sorted(evenDigitsList)


# sample = 'Sorting1234'
sample = raw_input()

#  Check
print "".join(fillLists(sample))