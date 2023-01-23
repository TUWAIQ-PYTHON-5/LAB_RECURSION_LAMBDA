
# 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:

def vowels_count (phrase : str) -> int:
    
    #base condition
    if len(phrase) == 0:
     return 0

    if phrase[0].lower() in ["a","e","o","i","u"]:
        return 1 + vowels_count(phrase[1:])
    else :
         return 0 + vowels_count(phrase[1:])

vowels_in_phrase = vowels_count("I love python")
print(vowels_in_phrase)



# 2) create a new list containing each number from the previous list mutliplied by itself.


num_list = [40, 35, 10, 15, 20]


num_list_mul =list(map(lambda x : x*x , num_list))
print("the new list mutliplied by itself : ", num_list_mul)




