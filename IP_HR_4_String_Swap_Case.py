inp='HackerRank.com presents "Pythonist 2".'

out = []

for i in inp:
    #print(i)
    if i.isupper():
        i=i.lower()
    elif i.islower():
        i=i.upper()
    #print(i)
    out.append(i)

print(''.join(out))


ip = 'this is a string'

m = ip.split(" ")
print('-'.join(m))

#Important string functions
#string = string[:5] + "k" + string[6:]