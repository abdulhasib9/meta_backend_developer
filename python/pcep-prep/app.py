senetence ="this is the most common interview question"
senetence_frequency={}

for x in senetence:
    if x in senetence_frequency:
        senetence_frequency[x] +=1
    else:
        senetence_frequency[x] =1
print(senetence_frequency)
from pprint import  pprint
pprint(senetence_frequency)
pprint(sorted(senetence_frequency.items(),key=lambda kv: kv[1],reverse=True))
sorted(senetence_frequency.items(),key=lambda kv: kv[1],reverse=True)
most_repeated = sorted(senetence_frequency.items(),key=lambda kv: kv[1],reverse=True)
print(most_repeated[0])