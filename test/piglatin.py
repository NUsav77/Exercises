p = str(input())
phrase = tuple(p.split())

piglatin = []

for word in phrase:
    temp = word[1:]+word[0]+'ay'
    piglatin.append(temp)

print(piglatin)