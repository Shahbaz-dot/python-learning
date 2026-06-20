# Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'.
f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("twinkle is persent in the content")

else:
    print("twnikle is not present in the contains")
f.close()

# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
import random

def game ():
    print ("You are playing the game..")
    score = random.randint (1, 62)
    # Fetch the hiscore
    with open ("hiscore.txt") as f:
        hiscore = f. read()
        if(hiscore!="") :
            hiscore = int(hiscore)
            
        else:
            hiscore = 0
        
        print (f"Your score: {score}")
        if(score>hiscore):
           # write this hiscore to the file
           with open ("hiscore.txt", "w") as f:
              f.write(str(score))

    return score
game()

# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 - year old.
def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} * {i} = {n*i}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 21):
    generateTable(i)

# A file containsa word "Donkey" multiple times. You need to write a program which replace this word with ##### by updating the same file.
word =  "Donkey"

with open("prac4.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("prac4.txt", "w") as f:
    f.write(contentNew)

# Repeat program 4 for a list of such words to be censored.
words =  ["Donkey", "bad", "bloodyfool"]

with open("prac4.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))
# contentNew = content.replace(word, "######")

with open("prac4.txt", "w") as f:
    f.write(content)

# Write a program to find out the line number where python is present from ques 6.
with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes python is persent. Line no: {lineno}")
        break
    lineno += 1

else:
    print("Nope python is not present")

# Write a program to make alcopy of a text file "this. txt"
with open("this.txt") as f:
    content = f.read()

with open("this_copy.txt", "w") as f:
    f.write(content)
