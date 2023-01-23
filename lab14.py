def words_vowels(word : str)->int:
    if len(word)==0:
        return 0
    if word[0].lower() in ["a" , "e" , "i" , "o" , "u"]:
        return 1+words_vowels(word[1:])
    else:
        return 0+words_vowels(word[1:])



count=words_vowels("I love python")
print(count)

number_list=[40,35, 10, 15, 20]
number_multbut=list(map(lambda x:x*x,number_list))
print(number_multbut)