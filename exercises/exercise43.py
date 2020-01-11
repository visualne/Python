import re
# 0 0 0
# 0 0 0
# 0 0 0

# $a
# t%
# ir!

# Tsi
# h%x
# i #
# sM
# $a
# t%
# ir!

#  Need a function that checks the length of the list
#  when the length of the list is determined it will
#  populate a certain list based on what position the
#  character is in.

#  This function adds entries in tempList to approrpiate
#  location in currentLists
def whatever(tempList,currentLists):
    pass

def combineFunction(someString,currentLists):
    #  Get Length of string
    lenOfString = len(someString)

    #  Code here to put each character in a separate list.
    tempList = map(list,someString)

    #  If currentList is zero. Take everything in that is in
    #  tempList and put it in currentList
    if len(currentLists) == 0:
        #  Adding each entry in tempList to currentList
        for letter in tempList:
            currentLists.append(letter)

    #  Checking to see if tempList is same size as currentLists
    #  if it is, it will add each entry in tempList to the
    #  appropriate location in currentLists
    elif len(currentLists) >= len(tempList):
        #  Adding each entry in tempList to the corresponding
        #  location in currentLists
        for i in range(len(tempList)):
            currentLists[i].append(tempList[i][0])

    else:
        pass

    return currentLists

sampleList = ['Tsi','h%x','i #','sM ','$a ','#t%','ir!']

#  tempList will hold each entry in each row
tempList = []

#  currentLists will hold each columns entries.
currentLists = []

#  Looping through each row in sample list and building
#  a list of columns with the combineFunction
for entry in sampleList:
    currentLists = combineFunction(entry,currentLists)

#  For loop to combine each of the words in the decoded message
tempWord = ''
for word in currentLists:
    tempWord = tempWord + ''.join(word)

#  For loop to replace the needed characters.
for val in re.finditer('\w+([^A-Za-z0-9]+)\w',tempWord,re.I):
   tempWord = tempWord.replace(val.group(1),' ')

print tempWord


#  Sample string that will be matched:
#  'This$#is% Matrix#%!'

# re.search('[A-Za-z0-9]+([^A-Za-z0-9]+)',sample).group()

# This$#is% Matrix#  %!


#  Goal replace symbols or spaces
#  between alphanumeric characters

#  Replace the symbols or spaces between two alphanumeric characters
#  \w[any_character]+\w ->







    # print currentLists
    # exit(1)
