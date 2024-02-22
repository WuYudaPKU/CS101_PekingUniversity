dict_vowel = ['A','O','Y','E','U','I',
              'a','o','y','e','u','i']
word=input()
list_word=list(word)
list_result=[]
for index,item in enumerate(list_word):
    if item not in dict_vowel:
        list_result.append(item.lower())
for index,item in enumerate(list_result):
     list_result[index] = "."+item
print("".join(list_result))