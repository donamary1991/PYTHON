import random  # random module is imported

name = input("Enter your name: ")
print(f"Welcome {name}! All the best.")

words_list = []
f = open("words_list", "r")
for i in f:
    words_list.append(i.rstrip("\n"))  # words list is added with words from the external file

word = random.choice(words_list)    # word is chosen at random from the words list
graphic = [
    """
            +-------+
            |
            |
            | 
            |
            |
         ==============
        """
    ,
    """
            +-------+
            |       |
            |      (0)
            | 
            |
            |
         ==============
        """
    ,
    """
            +-------+
            |       |
            |      (0)
            |       |
            |
            |
         ==============
        """
    ,
    """
            +-------+
            |       |
            |      (0)
            |      -|
            |
            |
         ==============
        """
    ,
    """
            +-------+
            |       |
            |      (0)
            |      -|-
            |
            |
         ==============
        """
    ,
    """
            +-------+
            |       |
            |      (0)
            |      -|-
            |      /
            |
         ==============
        """
    ,
    """
            +-------+
            |       |
            |      (0)
            |      -|-
            |      / \ 
            |
         ==============
        """]

display = "_" * len(word)  # initialises display with blank spaces equal to length of chosen word
life = 6
correct_guesses = []  # list created to fill the correctly guessed letters
guessed_letters_list = []  # list created to add all guessed letters

while life > 0:     # loop runs until user run out of lives or wins
    print("*" * 100)
    print(display)

    hangman = graphic[6 - life]
    print(hangman)  # prints the hangman as per lives remaining

    guess = input("Enter a letter: ")  # asks the user for input

    generated_word = ""

    if guess not in guessed_letters_list:  # if we have not guessed the letter previously
        guessed_letters_list.append(guess)

        if guess in word:  # if guessed letter is present in chosen word
            print(f"You have guessed the letter right. Lives left: {life}")

            for letter in word:  # iterate through each letter in the chosen word

                if letter in correct_guesses:  # if the letter was previously guessed correctly
                    generated_word += letter

                elif letter == guess:  # if the letter is the current guessed letter
                    correct_guesses.append(guess)
                    generated_word += letter

                else:  # if the letter is not yet guessed
                    generated_word += "_"
            display = generated_word

        else:  # if guessed letter is not present in chosen word
            life -= 1

            if life > 0:  # if user has not run out of lives
                print(f"You have guessed the letter wrong. Lives left: {life}.")

            else:  # if the user has run out of lives
                hangman = graphic[6 - life]
                print(hangman)  # prints the full hangman before exiting the while loop
                print(f"You have exhausted all lives. You lose.\nThe word is {word}.")

        if generated_word == word:  # if all blanks are filled with letters
            print(f"Congrats! The word {display} is completely guessed.")
            print("You have won.")
            break

    else:  # if we have guessed the letter previously
        print(f"You have already guessed that letter. Lives left: {life}")
