#find the character the occure more than other chracters 

from pprint import pprint
sentence ="this is how we find it for interview question"

character_frequency = {}

for x in sentence:
    if x in character_frequency:
        character_frequency[x] +=1
    else:
        character_frequency[x] =1

print(character_frequency)

char_listed=sorted(character_frequency.items(), key=lambda kv:kv[1],reverse=True)

pprint(char_listed)
print("----------------- Most used chracter is -----------------------")
print(char_listed[0])