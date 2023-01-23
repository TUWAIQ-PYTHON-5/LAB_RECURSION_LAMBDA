def vowels(phrase,num=0):
    if len(phrase)==0:
        return num
    else:
        if phrase[0]=="a" or phrase[0]=="A":
            num=1
            return num + vowels(phrase[1:])
        elif phrase[0]=="e" or phrase[0]=="E":
            num=1
            return num + vowels(phrase[1:])
        elif phrase[0]=="i" or phrase[0]=="I":
            num=1
            return num + vowels(phrase[1:])
        elif phrase[0]=="o" or phrase[0]=="O":
            num=1
            return num + vowels(phrase[1:])
        elif phrase[0]=="u" or phrase[0]=="U":
            num=1
            return num + vowels(phrase[1:])
        else:
            return num + vowels(phrase[1:])

'''
def vowels(phrase):
    if len(phrase)==0:
        return 0

    if:
        phrase[0].lower in ["a","e","i","o","u"] :
        return 1 + vowels(phrase[1:])
    else:
        return vowels(phrase[1:])

'''
result = vowels("I love python")
print(f"There are: {result}")

numberList = [40,35, 10, 15, 20]

multipliedNumbers = list(map(lambda number : number*number, numberList))

print(f"the new list is: {multipliedNumbers}")