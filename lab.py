def count_vowels(word):
    vowels = "aeiouAEIOU"
    if word == "":
     return 0
    elif word[0] in vowels:
     return 1 + count_vowels(word[1:])
    else:
      return 0 + count_vowels(word[1:])
print(count_vowels("I am an engineer"))



lst=[40,35, 10, 15, 20]
my_new_list=list(map(lambda n:n*n ,lst))
print(my_new_list)