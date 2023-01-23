


def Letter_vowels(word):
    if len(word)==0:
        return 0

    if word[0].lower()in["a","e","o","i","u"]:
        return 1 + Letter_vowels(word[1:])
    else:
        return 0 + Letter_vowels(word[1:])

vowles_in_word = Letter_vowels("i love python sO much")
print("vowles: ",vowles_in_word)

print("--------"*5)

numbers_list=[40,25,50,100]
numbers_list_multiplies = list (map(lambda x: x*x, numbers_list))
print("a list number is ", numbers_list_multiplies)