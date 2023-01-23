'''
Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:
Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase .
Example: given the phrase "I love python" , it should return : 4

Given a list of numbers : [40,35, 10, 15, 20]
create a new list containing each number from the list mutliplied by itself.
print the new list.
Hint: use map() with a lambda funciton
'''

def count_vowels(word : str)-> int:
   
    if len(word) == 0:
        return 0

    if  word[0].lower() in ["a" , "e" , "o" , "i" ,"u"]:
            return 1 + count_vowels(word[1:])
    else:
        return 0 + count_vowels(word[1:])

vowels_in_word = count_vowels("i love python s0 much")
print(vowels_in_word)


number_list = [40,35,10,15,20]
number_Multiplies = list(map(lambda e : e * e , number_list))

print(number_Multiplies)
    
    