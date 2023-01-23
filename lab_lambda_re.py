def vowels(word:str):

    if len(word) ==0:
          return 0
    if word [0].lower()in ["a","e","o","i","u"]:
        return 1 + vowels(word[1:])
    else:
        return 0+ vowels(word[1:] )

phrase=vowels("I love python")
print(phrase)






number_list=[40,35, 10, 15, 20]
new_list=list(map(lambda x:x*x,number_list))
print(new_list)

