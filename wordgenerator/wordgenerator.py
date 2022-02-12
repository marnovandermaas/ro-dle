wordfile = open('nohyphen.ro.txt')

# Populate words
words = []
for line in wordfile.readlines():
    words.append(line[0:5].lower())

# Replace ă with a
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

# Output validGuesses.ts
guessfile = open('validGuesses.ts', 'w')
guessfile.write('export const VALID_GUESSES = [\n')
for word in sorted(guesses):
    guessfile.write("  '" + word + "',\n")
guessfile.write(']\n')

# Process most common Romanian words
import csv
commonfile = open('2000MostCommonRomanianWords.csv')
csvFile = csv.reader(commonfile)
answers = set()
for line in csvFile:
    word = line[1]
    if len(word) == 5:
        answers.add(word.lower().replace('ă', 'a'))

# Output wordlist.ts
answerfile = open('wordlist.ts', 'w')
answerfile.write('export const WORDS = [\n')
for word in answers:
    answerfile.write("  '" + word + "',\n")
answerfile.write(']\n')
