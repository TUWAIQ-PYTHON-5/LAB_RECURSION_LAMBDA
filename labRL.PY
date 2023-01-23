#1
def isVowel(ch):
    return ch.lower() in ['a', 'e', 'i', 'o', 'u']
 

def countVowels(str):
    count = 0
    for i in range(len(str)):
 
       
        if isVowel(str[i]):
            count += 1
    return count

str = 'i love python'
print(countVowels(str))


#2
number_list = [40,35, 10, 15, 20]

numbermult =list(map(lambda x : x*x, number_list))
print("a list of multipled :", numbermult)
