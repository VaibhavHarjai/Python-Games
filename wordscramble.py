import random

def scramble_word(word):
    """
    Shuffle the letters of the input word and return the scrambled version.
    """
    word_letters = list(word)
    random.shuffle(word_letters)
    return ''.join(word_letters)

def play_game():
    # List of words to choose from
    words = ["python", "programming", "scramble", "challenge", "developer", "software", "coding", "algorithm", "computer", "science", "csharp"]
    
    # Randomly select a word from the list
    chosen_word = random.choice(words)
    scrambled = scramble_word(chosen_word)
    
    print("\nWelcome to the Word Scramble Game!")
    print("\nUnscramble the letters to form a valid word.")
    print("\nScrambled word:", scrambled)
    
    attempts = 3  # Number of attempts allowed
    while attempts > 0:
        guess = input("\nEnter your guess: ").strip().lower()
        
        if guess == chosen_word:
            print("\nCongratulations! You guessed correctly!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"\nIncorrect. Try again! Attempts remaining: {attempts}")
            else:
                print(f"\nSorry, you've run out of attempts. The correct word was: '{chosen_word}'.")
            
            print("\nThanks for playing!")
                
if __name__ == "__main__":
    play_game()