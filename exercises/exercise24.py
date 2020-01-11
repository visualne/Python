#  Given a string S - Find all substrings
#  One player has to make words with consants [bcdfghjklmnpqrstvwxyz]
#  Another player has to make work with vowels [aeiou]

#  You get one point each time the substring appears in the word.

#  Brute force every combination of indexes? And then run a search
#  against each of those substrings?
# 0,0
# 0,1
# 0,2
# 0,3
# 0,4
# 0,5
import re

def fillDictionary(playerDictionary,matchObject):
    if matchObject:
        if matchObject.group() in playerDictionary:
            playerDictionary[matchObject.group()] = \
                playerDictionary[matchObject.group()] + 1

            #  Returning new dictionary
            return playerDictionary
        else:
            playerDictionary[matchObject.group()] = 1

            #  Returning new dictionary
            return playerDictionary


s = 'banana'

#  Create a dictionary the keep track of duplicates
#  ex) subStringDictionary = {substring: count}
subStringDictionary = {}

#  Dictionary here called player1
player1Dictionary = {}

#  Dictionary here called player2
player2Dictionary = {}

for i in range(len(s)+1):
    for j in range(len(s)+1):
    #  If second index is less then current index pass
        if i <= j:
            #  If statement to check to see if indexes are the same.
            #  if they are then the substring will be checked as follows
            #  ex) string[index]
            if i == j and i != len(s):
                #  Checking substring for words that begin with
                #  consants.
                matchCon = re.match(r'^[bcdfghjklmnpqrstvwxyz]',s[i])

                #  Another match here. matchVowel
                matchVowel = re.match(r'^[aeiou]',s[i])

                if matchCon:
                    player1Dictionary = fillDictionary(player1Dictionary\
                                                       ,matchCon)
                elif matchVowel:
                    #  Filling player2 dictionary appropriately.
                    player2Dictionary = fillDictionary(player2Dictionary,\
                                                       matchVowel)
                else:
                    pass

            else:
                #  Checking substring for words that begin with
                #  consants.
                matchCon = re.match(r'^[bcdfghjklmnpqrstvwxyz]\w+',s[i:j])

                #  Another match here. matchVowel
                matchVowel = re.match(r'^[aeiou]\w{1,}',s[i:j])

                if matchCon:
                    #  Filling player1 dictionary appropriately.
                    player1Dictionary = fillDictionary(player1Dictionary,\
                                                               matchCon)
                    #  Filling player2 dictionary appropriately.
                elif matchVowel:
                    #  Filling player2 dictionary appropriately.
                    player2Dictionary = fillDictionary(player2Dictionary,\
                                                       matchVowel)
                else:
                    pass
        else:
            pass


for val in player2Dictionary.items():
    print val
#  else print out the two of them here.

# 1,1
# 1,2
# 1,3
# 1,4
# 1,5

# 2,2
# 2,3
# 2,4
# 2,5

# 3,3
# 3,4
# 3,5

# 4,4
# 4,5

# 5,5