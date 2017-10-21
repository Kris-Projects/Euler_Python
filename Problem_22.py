"""
Using Problem_22.txt, a 46K text file containing over
five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical
value for each name, multiply this value by its
alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical
order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a
score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
#########################SOLUTION#########################
with open('Problem_22.txt', 'r') as f:
    g = f.read()

g = g.split(',')
names = [name.strip('"') for name in g]
names.sort()

total = 0
for i in range(len(names)):
    score = 0
    for word in names[i]:
        score += ord(word) - 64
    score *= (i+1)
    total += score

print(total)