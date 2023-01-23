def recVowelCount(s):

    vowels = "aeiouAEIOU"
    if s == "":
        return 0
    elif s[0] in vowels:
        return 1 + recVowelCount(s[1:])
    else:
        return 0 + recVowelCount(s[1:])
        


print(recVowelCount("I love python"))

numbers_list = [40 , 25 , 50 ,100]
numbers_list_multi = list(map(lambda x : x*x , numbers_list))
print(numbers_list_multi)
