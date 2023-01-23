# define a recursive function to count the consecutive numbers


def count_Vovels(phrase :str)-> int:

     if len(phrase) == 0:
         return 0

     if phrase[0].lower() in ["a", "e", "i", "o", "u"]:
         return 1+count_Vovels(phrase[1:])
     else:
         return 0+ count_Vovels(phrase[1:])


vowels_in_phrase = count_Vovels(" I love python so much")
print(vowels_in_phrase)

#lambda Functions
multiply = [40, 25,50,100]
numbers_list_multiply = list(map(lambda x : x*x,multiply))
print("the new list is ",multiply)



