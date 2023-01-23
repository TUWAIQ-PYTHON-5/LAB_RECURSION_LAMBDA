def vowels_char (phrase : str) -> int:
    if len(phrase)==0:
        return 0
    
    if phrase[0].lower() in ["a","e","i","o","u"]:
        return 1+ vowels_char(phrase[1:])
    else :
        return vowels_char(phrase[1:])
    
vowels_in_phrase = vowels_char("i love python")
    
print (vowels_in_phrase)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

number_list= [40,35, 10, 15, 20]
number_list_multiblied=list(map(lambda x: x**2 , number_list))
print("the list of multiblied number = " , number_list_multiblied)
