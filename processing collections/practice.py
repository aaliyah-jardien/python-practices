# STEP 1 Remove the vowels
# You have a list of words and a list of vowels (enter these in the shell):
words = ['eat','lockdown','python','learn','submit','review','grade']
vowels = ['a','e','i','o','u']
no_vowels = []

for word in words:
    for character in word:
        if character in vowels:
            word = word.replace(character,'')
    no_vowels.append(word)
print(no_vowels) #['t', 'lckdwn', 'pythn', 'lrn', 'sbmt', 'rvw', 'grd']

remove_vowels()

# Change this to use lambda functions, filter() and map(), i.e. there
# must be no for loops. Tip: first define a remove_vowels(word) function
# that will remove the vowels from a single word.

"""
STEP One-liner?

Can you see a way to remove the need for the separate remove_vowels function, and get to single line of code that does everything?

Do you think ""such a single line of code is easier to understand, and maintain in future?
"""