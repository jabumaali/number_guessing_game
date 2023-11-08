"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
By: Jabr Abumaali
Started: Nov 8, 2023
Completed: Nov 8, 2023
--------------------------------
"""
import random
import statistics

def start_game():
    print("Welcome to the Number Guessing Game!")

    records = []
    while True:
        answer = random.randint(1,100)
        attempts = 0

        print("Please guess the number between 1 and 100!")
        while True:
            try:
                x = int(input())
                if x not in range(1,100):
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
                        records.append(attempts)
                        records.sort()
                        mean = round(statistics.mean(records), 2)
                        median = statistics.median(records)
                        mode = statistics.mode(records)
                        print("Mean: {}\nMedian: {}\nMode: {}\n".format(mean, median, mode))
                        break
            except ValueError:
                print("Please enter a number between 1 and 100.")
            
        while x != "y" and x != "n":
            x = input("Would you like to play again? y/n: ")
        if x == "n":
            break
        
        print("High score: {}".format(min(records)))
        
    print("Thanks for playing!")


start_game()
