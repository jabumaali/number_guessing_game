"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
By: Jabr Abumaali
Started: Nov 8, 2023
Completed: Nov 9, 2023
--------------------------------
"""
import random
import statistics

def start_game():
    print("Welcome to the Number Guessing Game!")

    # Initalize record of scores (list).
    records = []

    # This outer while runs once per game, and only
    # ends when the user finally enters "n".
    while True:
        
        # Generate a random number, and
        # start the number of attempts at 0.
        answer = random.randint(1,100)
        attempts = 0
        print("Please guess the number between 1 and 100!")

        # This inner while continuously prompts the
        # user until they find the correct answer.
        while True:
            try:
                x = int(input())
                if x not in range(1,101):
                    print("Please enter a number between 1 and 100.")
                else:
                    attempts += 1
                    if x < answer:
                        print("Too low.")
                    if x > answer:
                        print("Too high.")
                    if x == answer:
                        print("You guessed it: {}!".format(answer))
                        print("You won in {} attempts.\n".format(attempts))
                        # Notify user of new record!
                        if records and (attempts < min(records)):
                            print("New high score!")
                        records.append(attempts)
                        records.sort()
                        mean = round(statistics.mean(records), 2)
                        median = statistics.median(records)
                        mode = statistics.mode(records)
                        print(f"Mean: {mean:.2f}\nMedian: {median}\nMode: {mode}\n")
                        # Only break when the correct answer is reached
                        break
            except ValueError:
                print("Please enter a number between 1 and 100.")

        # Wait for "y" or "n"
        while x != "y" and x != "n":
            x = input("Would you like to play again? y/n: ")

        # Only end the game when "n" is chosen.
        if x == "n":
            break

        # Show 
        print("High score: {}".format(min(records)))
        
    print("Thanks for playing!")


start_game()
