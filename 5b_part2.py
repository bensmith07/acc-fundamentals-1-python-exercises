import random

# Initialize the play_again variable
# Start sentinel loop to allow plaer to continue playing until they decide to stop
play_again = 'Y'
while play_again == 'Y' or play_again == 'y':

    # Initialize guess_count accumulator
    guess_count = 0

    # Generate a random number between 1 and 1000
    number = random.randint(1, 1000)

    # Initialize guess variable and
    # begin loop to continue taking guesses until the player guesses the number
    guess = 1001
    while guess != number:

        # Prompt the player to guess a number
        guess = int(input('Guess a number between 1 and 1000: '))

        # Keep track of the number of guesses
        guess_count += 1

        # Test the guess and provide feedback to the player
        if guess > number+10:                                   # If the player’s guess is higher than the number
            print('Too High!')                                  # generated then display the message “Too High!”
            print()                                         
        elif guess > number and guess <= number+10:             # If the player’s guess is within a 10-point difference
            print('Getting warm but still high!')               # of the number generated but higher than the number generated,
            print()                                             # then give the message “Getting warm but still high!”
   
        elif guess < number-10:                                 # If the player’s guess is lower than the number
            print('Too Low!')                                   # generated then display the message “Too Low!”
            print()                                         
        elif guess < number and guess >= number-10:             # If the player’s guess is within a 10 point difference
            print('Getting warm but still Low!')                # of the number generated but lower than the number generated,
            print()                                             # then give the message “Getting warm but still Low!”

    # Once the player guesses the number, provide a congratulatory message
    # including the number of guesses it took them
    print()
    print('Good job! You guessed the number in ', guess_count, 'tries!')
    print()

    # Ask the player if they would like to play again
    play_again = input('Would you like to play again? (Enter "Y" for YES): ')
    print()

print('See you next time! Goodbye.')
