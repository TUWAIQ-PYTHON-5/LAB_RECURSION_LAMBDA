

def vowelByRecursion(txt:str)->int:
    if (txt == ''): return 0
    #vCount:int= (1 if txt[0] in 'AaEeIiOoUu' else 0) + vowelByRecursion(txt[1:])
    #print(vCount)
    #return vCount
    return (1 if txt[0] in 'AaEeIiOoUu' else 0) + vowelByRecursion(txt[1:])

print(vowelByRecursion("I love python"))
print("#"*18)

numList= [40,35,10,15,20]
mNumList= list(map(lambda x : x*x ,numList[1:]))
print("The Result List is: ", numList)