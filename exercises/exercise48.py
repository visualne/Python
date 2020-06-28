import math
#  Take in word or words and remove all spaces from the words or words.
def check_words(words):

    #  Hard coding facebook dictionary
    facebook_char_dict = {
        'f':1,
        'a':1,
        'c':1,
        'e':1,
        'b':1,
        'o':2,
        'k':1
    }

    #  Removing spaces from word. That will F things up if we don't.
    words = words.replace(' ','')

    words_char_dict = {}

    #  Creating character count dictionary based on word or words sent in.
    for char in words:
        if char in words_char_dict:
            words_char_dict[char] = words_char_dict[char] + 1
        else:
            words_char_dict[char] = 1


    #  Initializing number of stickers to buy
    num_of_stickers = 0

    #  For loop to find compare facebook_char_dict keys against words_char_dict
    for char in words_char_dict:
        if char in facebook_char_dict:
            #  The value is produced here is the number of stickers that would
            #  need to be bought to produce the number of characters sent into the function.
            value = math.ceil(words_char_dict[char] / facebook_char_dict[char])

            #  This if statement finds the greatest number of stickers found so far.
            if value > num_of_stickers:
                num_of_stickers = value

    #  Printing the largest amount of stickers found.
    print(num_of_stickers)


check_words('ffacebook')



