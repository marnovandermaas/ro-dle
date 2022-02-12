wordfile = open('nohyphen.ro.txt')

words = []
for line in wordfile.readlines():
    words.append(line[0:5].lower())

total = 0
alreadyin = 0
guesses = set()
for word in words:
    newword = word
    if 'ă' in word:
        total += 1
        newword = word.replace('ă', 'a')
        if newword in words:
            alreadyin += 1
            continue
    guesses.add(newword)

print('Total words with ă is ' + str(total) + ' of which ' + str(alreadyin) + ' exist already in the list when substituting with a.')

guessfile = open('validGuesses.ts', 'w')
guessfile.write('export const VALID_GUESSES = [\n')
for word in sorted(guesses):
    guessfile.write("  '" + word + "',\n")
guessfile.write(']\n')

import csv
commonfile = open('2000MostCommonRomanianWords.csv')
csvFile = csv.reader(commonfile)
for line in csvFile:
    word = line[1]
    if len(word) == 5:
        print(word)

