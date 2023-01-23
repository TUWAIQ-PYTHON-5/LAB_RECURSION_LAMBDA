def word_char(word:str):
       if len(word)==0:
        return 0
       if word[0].lower() in ['a','e',"i",'o','u']:
        return 1 + word_char(word[1:])
       else:
        return 0+ word_char(word[1:])
        
print(word_char("my name is sultan Alshahrani"))




number_list=[40,35,10,15,20]

number=list(map(lambda x:x*x ,number_list))

print(number)
