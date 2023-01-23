def count_vowels(phrase) :
    length = len(phrase)
    if length == 0 :
        return 0
    if phrase[0].lower() in ["a", "e", "i", "o", "u"]:
        return 1 + count_vowels(phrase[1:])
    return  count_vowels(phrase[1:])

print(count_vowels("i love python"))

numbersList = [40,35, 10, 15, 20]
newList = list(map(lambda x : x*x, numbersList))
print(newList)



