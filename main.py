try:
    def check_vowels_litter(word:str):
        litter_check=["a","e","i","o","u"]
        if len(word)==0:
            return 0
        if word[0].lower() in litter_check:
            return 1+ check_vowels_litter(word[1:])
        else:
            return 0+ check_vowels_litter(word[1:])
            
    word:str="I love python".lower()
    print(check_vowels_litter(word))

    n1:list=[40,35, 10, 15, 20]
    numbers = list(map(lambda x : x*x , n1))
    print(numbers)

except Exception as e:
    print(e)
