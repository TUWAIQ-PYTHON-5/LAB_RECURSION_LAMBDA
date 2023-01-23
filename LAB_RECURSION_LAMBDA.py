#Returns count of vowels in str
def count_vowels(phrase: str)-> int:

   if len(phrase)==0:
       return 0

   if phrase[0].lower() in ["a","e","o","i","o"]:
        return 1+count_vowels(phrase[1:])
   else :
        return 0+ count_vowels(phrase[1:])

vowels_in_phrase=count_vowels("I love python")
print(vowels_in_phrase)

#list mutliplied by itself.
numbers_list=[40,25,50,100]
numbers_list_multiplied =list( map(lambda x :x*x, numbers_list))
print(" The new list is ", numbers_list_multiplied)