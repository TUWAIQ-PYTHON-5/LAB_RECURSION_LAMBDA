# 1


def count_Vowels(phrase : str) -> int:

    if len(phrase) == 0:
         return 0

    if phrase[0].lower() in ['A', 'E', 'I', 'O', 'U']:
        return 1 + count_Vowels(phrase[1:])

    else :
        return 0 + count_Vowels(phrase[1:])

vowels_in_phrase = count_Vowels("i love python code ")
print(vowels_in_phrase)


#2 


list_numbers = [40,35, 10, 15, 20]
multiply_numbers =list (map (lambda x: x*x ,list_numbers ))
print("a list bultiplyed by numbers  is :", list_numbers)






