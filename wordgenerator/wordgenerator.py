wordfile = open('nohyphen.ro.txt')
outfile = open('noabreve.ro.txt', 'w')

words = []

for line in wordfile.readlines():
    words.append(line[0:5].lower())

total = 0
alreadyin = 0
for word in words:
    if 'ă' in word:
        total += 1
        if word.replace('ă', 'a') not in words:
            print('+' + word)
            outfile.write(word.replace('ă', 'a') + '\n')
        else:
            print('-' + word)
            alreadyin += 1
    else:
        outfile.write(word + '\n')

print('Total words with ă is ' + str(total) + ' of which ' + str(alreadyin) + ' exist already in the list when substituting with a.')

