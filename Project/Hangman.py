from random import choice
from time import sleep
from os import system
words = []

print('This is the game "Hangman".\nYou need to guess a word by entering letters from the keyboard.')
while True:
    print("Are you ready?")
    ans = input(">>> ")
    if ans.lower() == "no":
        exit(0)
    elif ans.lower() == "yes":
        break
system("cls")

f = open('dictionary.txt')
for i in f.readlines():
    if i[-1] == '\n':
        i = i[:-1]
    words.append(i)
f.close()

while True:
    word = choice(words)
    alphabet = []

    letters =[]
    for i in range(len(word)):
        letters.append('_')
    life = 11
    game = True
    let =0
    end =0
    # слова
    while game and life>0:
        print("You have", life, "life")
        print(''.join(letters))
        letter = input("Enter a word or a letter: ")
        letter = letter.lower()
        system("cls")
        if letter in alphabet:
            print("This letter was")
        elif len(letter)>1:
            # правильные слова
            if letter == word:
                game = False
            else:
                # неправильные слова
                life = 0
        else:
            alphabet.append(letter)
            # правильные буквы
            for i in range(len(word)):
                if letter == word[i]:
                    letters[i] = letter
                    end +=1
                # неправильные буквы
                else:
                    let+=1
                    if let == len(word):
                        life -= 1
                        let =0
            let = 0
        # конец цикла
        if end == len(word):
            game = False
    # конец
    print("This word is", word)
    if life == 0:
        print("Game over")
    else:
        print("You win!")
    sleep(5)
    system("cls")
    while True:
        print("Do you want to play again?")
        ans = input(">>> ")
        if ans.lower() == "no":
            exit(0)
        elif ans.lower() == "yes":
            break
