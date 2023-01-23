def fun (word : str) -> int:
    
    if len(word) == 0:
        return 0


    if word[0].lower() in ["a","e","i","o","u"]:
        return 1 + fun(word[1:])

    else:
        return 0+ fun(word[1:])


print(fun("I love python "))


#_______________________________#



number_list = [40,35, 10, 15, 20 , 100]

number = list(map(lambda x:x*x , number_list))

print(number)
