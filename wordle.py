from random import *
words = ["hello","world","ready","tires","quilt","grape","rhyme","fresh","makes","swing","dusky","wring","blink","theme","joker","craft"]


def guess(user_guess,todays_word):
    if len(user_guess)!=5:
        guess(input("Guess a 5 letter word: "),words[0])
    if user_guess == todays_word:
            print("Congratulations you got the correct word, " + todays_word + ", in 1 turn!")
            exit()
    turn_counter = 1
    letter_index =-1
    answer = []
    while turn_counter < 6:        
        for letter in todays_word:
            letter_index += 1
            if user_guess[letter_index] in todays_word:
                if user_guess[letter_index] == letter:
                    answer.append("Green")
                else:
                    answer.append("Yellow")
            else:
                answer.append("Grey")
        print(answer)
        
        turn_counter += 1
        print("Turn " + str(turn_counter) + " of 6.")

        user_guess = input("Guess a 5 letter word: ")
        if len(user_guess)!=5:
            while len(user_guess)!=5:
                user_guess = input("Guess a 5 letter word: ")

        letter_index = -1
        answer = []
        
        if user_guess == todays_word:
            print("Congratulations you got the correct word, " + todays_word + ", in " + str(turn_counter) + " turns!")
            exit()
        
        
    else:
        print("You have run out of turns. The correct word was " + todays_word + "!")


guess(input("Guess a 5 letter word: "),choice(words))