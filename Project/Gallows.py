from random import choice
words = ["deprecative","disproportion","aquarium","conductor","checkmate","eloquent","currant","acolyte","catacomb","effeminacy","computer","access","bookcase","communicable","ending","autumn","exemplary","floral","freeman","boaster","emblematic","fortune","beautiful","calabash","bottommost","copulation","changeability","calamity","bloody","antedate","dignity","babyhood","deliberatea","crisis","comfortless","fiddlededee","barefoot","decision"]
word = choice(words)
print("You have 11 life")
letters =[]
for i in range(len(word)):
    letters.append('_')
print(''.join(letters))
life = 11
game = True
let =0
end =0
# слова
while game and life>0:
    letter = input("Enter a word or a letter: ")
    letter = letter.lower()
    if len(letter)>1:
        # правильные слова
        if letter == word:
            game = False
        else:
            # неправильные слова
            life -= 1
            print("You have",life,'life')
    else:
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
                    print("You have", life, 'life')
        print(''.join(letters))
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
