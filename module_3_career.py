#  Write a function that takes a string input: 'str'
#  Return the number / count of vowels in the input string.
#  For the purpose of this assignment, consider 'a', 'e', 'i', 'o' and 'u'
#  as vowels
#  the input string will consist of lower case letters

def count_the_vowels(str):
    str = input("Enter a word. Any word. Scrabble rules need not apply: ")
    # 1. Initialize a counter variable to keep track.
    count_vowels = 0

    #2. Use a for loop to cycle through the letters in the string.
    for v in str:
        if (v == 'a') or (v == 'e') or (v == 'i') or (v == 'o') or (v == 'u') or (v == 'A') or (v == 'E') or (v == 'I') or (v == 'O') or (v == 'U'):
            count_vowels += 1
    
    if count_vowels == 1:
        return(f"There is {count_vowels} vowel in the 'word' you entered.")
    if count_vowels != 1:
        return(f"There are {count_vowels} vowels in the 'word' you entered.")