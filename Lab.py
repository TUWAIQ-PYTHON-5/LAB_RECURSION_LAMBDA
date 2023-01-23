# 1) Using recursion, if given a word/phrase 
# return how many vowels(a,e,i,o,u) are in that phrase or word:

def count_vowels_numbers(s)-> int :
    vowels = "aeiouAEIOU"
    if s == "":
        return 0
    elif s[0] in vowels:
        return 1 + count_vowels_numbers(s[1:])
    else:
        return 0 + count_vowels_numbers(s[1:])

    print("Number of vowels in the given string is: ", )

print (count_vowels_numbers("I love python"))


## 2) Given a list of numbers : [40,35, 10, 15, 20]

numbers_list =[40,35, 10, 15, 20]
numbers_list_multiplies = list(map(lambda x : x*x , numbers_list))
print("a list of multiplies numbers by iteself is : " , numbers_list_multiplies)
