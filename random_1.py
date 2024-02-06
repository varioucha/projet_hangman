def display_word_state(word, guessed_letters):
    # Initialize the displayed word as a list of underscores or letters
    displayed_word = [letter if letter in guessed_letters else '_' for letter in word]

    # Join the list elements into a string for display
    displayed_word_str = ' '.join(displayed_word)

    # Print the current state of the word
    print("Current word: " + displayed_word_str)

# Example usage
word = "hangman"
guessed_letters = ['a', 'n']  # Example list of correctly guessed letters

# Call the function to display the word state
display_word_state(word, guessed_letters)
