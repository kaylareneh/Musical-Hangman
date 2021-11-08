import random
import string 
from words import artist 
from hangman_image import hangman_pic
from music import play_music
from colorama import Fore
play_music()


win = 0

def given_word(artist):
    word = random.choice(artist) 
    return word.lower()


def game():
    guesses = 7
    word = given_word(artist)
    word_letters = set(word) 
    letters = set(string.ascii_lowercase)
    given_letters = set()  

# MAYBE ASSIGNING A HINT TO A SPECIFIC VARIABLE TO SO THAT WHEN RANDOM GIVES THEM THAT ARTIST OR SONG THEY ARE ABLE TO GATHER HINTS ON THE SPECIFIC ARITST, BUT THIS ALSO MAY NEED TO BE IN THE WHILE LOOP. 
    
    while len(word_letters) > 0 and guesses > 0:
        print(Fore.YELLOW + 'Listen to the music to guess the artist/song.')
        print('You got', guesses, 'guesses left')
#MAYBE ADDING OPTIONS THAT VARY BETWEEN AMOUNT OF GUESSES LEFT TO MAKE DIFFERENT PRINT STATEMENTS OCCUR.        
        word_list = [word_let if word_let in given_letters else '-' for word_let in word]
        print(hangman_pic[guesses])
        print('Random Word: ', ' '.join(word_list))
        given_letter = input('Guess a letter: ').lower()
        if given_letter in letters - given_letters:
            given_letters.add(given_letter)
            if given_letter in word_letters:
                word_letters.remove(given_letter)
                print('')

            else:
                guesses = guesses - 1  
                print('Your letter,', given_letter, 'is not in the word.')

        elif given_letter in given_letters:
            print('You have already used that letter. Guess another letter.')

        else:
            print('That is not a valid letter.')
            
    if guesses == 0:
        print('You had more potential than that :( PLAY AGAIN')
    else:
        print('See I knew you were smart!', word, 'is the correct guess!!')
        


 
if __name__ == '__main__':
    game()