import random
import time
with open("words.txt", 'r') as file:
    lines = file.readlines()
wordlist = []
for line in lines:
    wordlist.append(str(line.strip()))
wordcount = int(input("How many words do you want to type?"))
score = 0
start = time.perf_counter()
for x in range(wordcount):
    word = random.choice(wordlist)
    print(word)
    if input("Type word: ") == word:
        score += 1
end = time.perf_counter()
timetaken = end - start
print("{:.2f}".format((score/wordcount)*100)+'% accuracy')
print("{:.2f}".format((wordcount/timetaken)*60)+'WPM')