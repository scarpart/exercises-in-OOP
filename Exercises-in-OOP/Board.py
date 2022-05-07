class Board():
    """Creates the board for an object oriented hangman game"""
    def __init__(self, word):
        # Initializes the board. self._coded_word refers to the form of the word that is to be displayed to the player,
        # i.e. a hidden word that is to be guessed. It clears up as the player correctly guesses the letters.
        self._word = word
        self._index = 0 # This will be used on the update_guess method
        self._lost_limbs = [" "] * 6 # This will be used to show the body parts of the hanged man when the player guesses incorrectly
        self._coded_word = ""
        self._already_guessed = ""
        for letter in word:
            if letter.isalpha():
                self._coded_word += "-"
            else:
                self._coded_word += " "
    
    def create_board(self):
        # Prints the "board", that is, the post, noose, body and coded word, 
        # as well as the letters that have already been guessed.
        print(".--¬")
        print("|  {}              guessed letters: {}".format(self._lost_limbs[0], self._already_guessed))
        print("| {}{}{}".format(self._lost_limbs[1], self._lost_limbs[2], self._lost_limbs[3]))
        print("| {} {}".format(self._lost_limbs[4], self._lost_limbs[5]))
        print("|")
        print("|__  Make a guess! --> " + (self._coded_word))
    
    def update_guess(self, letter):
        # Method used to update self._coded_word such that the correctly guessed letters show up.
        bodyparts = ["O", "/", "|", "\\", "/", "\\"] 
        placeholder_list = list(self._coded_word)
        letter = letter.lower()

        # if the letter has already been tried, it will count as an error.
        if letter in self._word.lower() and letter not in self._already_guessed:
            for i, string in enumerate(self._word):
                if string.lower() == letter:
                    placeholder_list[i] = letter
            
            # adds letter to the 'already guessed' list
            if len(self._already_guessed) != 0:
                self._already_guessed += ", " + letter
            else:
                self._already_guessed += letter
            
        else:
            # adds to the list of lost limbs that will be displayed on screen
            self._lost_limbs[self._index] = bodyparts[self._index]
            self._index += 1

            # adds letter to the 'already guessed' list
            if letter not in self._already_guessed:
                if len(self._already_guessed) != 0:
                    self._already_guessed += ", " + letter
                else:
                    self._already_guessed += letter
            

        self._coded_word = ''.join(placeholder_list)

    def has_game_ended(self):
        # OoT = Out of Tries
        # GiR = Got it Right
        if self._index == 6:
            return True, "OoT"
        elif self._coded_word.count("-") == 0:
            return True, "GiR"
        else:
            return False, ""