# How on earth can this be optimized? You have to check
# each word in note and see if it is in magazine. Maybe sort
# both lists ahead of time?

def checkWords(magazine,note):
    #  For loop to fill the magazineWords dictionary appropriately.
    for word in magazine:
        #  Checking to see if the word is already in the dictionary.
        if word not in magazineWords.keys():
            magazineWords[word] = 1
        else:
            magazineWords[word] = magazineWords[word] + 1

    #  For loop to check the words in the notes list against the keys
    #  in the magazineWords dictionary.
    for word in note:
        if word not in magazineWords.keys():
            print 'Sorry the word: ' + word + ' is not in the magazine.'
            return 'No'
        else:
            #  Check to see what count is of the word.
            if not magazineWords[word] > 0:
                print 'Sorry there is not enough of the word: ' + word + ' in the'\
                + ' magazine.'
                return 'No'
            else:
                #  Decrement the number of times that word
                #  was seen so far in the note word list.
                magazineWords[word] = magazineWords[word] - 1

    #  If the program completely makes it through the above for loop that means
    #  there are enough words in the magazine to cover what is in the note.
    return 'Yes'


def checkStrings(stringOne,stringTwo):
    #  Determine what string is the longest - this will be the outter
    #  for loop

    for char in stringOne:
        if char in stringTwo:
            return 'YES'

    return 'NO'




    #  Check each letter of longest string against the string
    #  that is less then or equal to the longest string.


    pass




#  Magazine array
magazine = ['sally','sells','sea','shells','down','by','the','sea']

#  note
note = ['sea','sells','down','shells']

#  Filling dictionary with magazine values
magazineWords = {}

print checkWords(magazine,note)







