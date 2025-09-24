# Python Program to illustrate
# Hangman Game
import random

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')
word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')

    # In ra các dấu gạch dưới cho từng chữ cái
    print(' '.join(['_' for _ in word]))

    chances = len(word) + 2
    guessed_letters = set()
    flag = False

    try:
        while chances > 0 and not flag:
            print(f"\nBạn còn {chances} lần đoán.")
            guess = input('Enter a letter to guess: ').lower()

            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) != 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in guessed_letters:
                print('You have already guessed that letter')
                continue

            guessed_letters.add(guess)

            # In ra trạng thái hiện tại của từ
            display = ''
            for char in word:
                if char in guessed_letters:
                    display += char + ' '
                else:
                    display += '_ '
            print(display.strip())

            # Kiểm tra thắng
            if all(char in guessed_letters for char in word):
                print(f"\nThe word is: {word}")
                print('Congratulations, You won!')
                flag = True
                break

            chances -= 1

        if not flag:
            print('\nYou lost! Try again..')
            print(f'The word was {word}')

    except KeyboardInterrupt:
        print('\nBye! Try again.')
        exit()