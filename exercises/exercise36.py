def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score = score + 1
    return score


sentence = 'programming is awesome'
words = sentence.split()
print score_words(words)



# The score of a single word is 2 if the word contains an even number of vowels.
# Otherwise, the score of this word is 1. The score for the whole list of words
# is the sum of scores of all words in the list.
#
# Debug the given function score_words such that it returns a correct score.
# Your function will be tested on several cases by the locked template code.