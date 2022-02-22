#Simple Number Guessing Game (CLI Version)
#Author : Glenny Walean

from random import randint
import os
clear = lambda: os.system('clear')

def main_menu():
    while(True):
        clear()
        print("    _   __                __                            \n   / | / /_  ______ ___  / /_  ___  ____________________\n  /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/ ___/ ___/ ___/\n / /|  / /_/ / / / / / / /_/ /  __/ /  (__  |__  |__  )\n/_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/  /____/____/____/\n")
        print("Simple Number Guessing Game - [Glenny Walean]\n")
        
        print("[1]  Play")
        print("[2]  About The Author")
        print("[3]  Quit\n")

        menu = input("input : ")
        if(menu == '1'):
            play()
        elif(menu == '2'):
            about_the_author()
        elif(menu == '3'):
            exit()
        else:
            print("\nError : invalid input.")
            input("\n\n\t<<<press ENTER to continue>>>")

def play():
    clear()
    print("Select Difficulty")
    print("[1]  Easy")
    print("[2]  Normal")
    print("[3]  Hard")
    print("[4]  Nightmare")

    diff = input("input : ")
    if(diff == '1'):
        end = 100
        lives = 10
    elif(diff == '2'):
        end = 100
        lives = 5
    elif(diff == '3'):
        end = 1000
        lives = 10
    elif(diff == '4'):
        end = 1000
        lives = 5
    else:
        print("\nError : invalid input.")
        input("\n\n\t<<<press ENTER to continue>>>")
        main_menu()

    random = randint(0, end)
    value = random

    answer = -1
    while(answer != value):
        clear()
        print("❤️  : {}\n".format(lives-1))
        answer = int(input("input number (0-{}) : ".format(end)))
        
        if(answer > value):
            print("\nToo High!")
            lives = lives - 1
        elif(answer < value):
            print("\nToo Low!")
            lives = lives - 1
        elif(answer == value):
            print("\nCorrect!")

        input("\n\n\n\n\n\t<<<press ENTER to continue>>>")

        if(lives == 0):
            clear()
            print("Game Over!")
            print("\n\nCorrect Answer : {}".format(value))
            input("\n\n\n\n\n\t<<<press ENTER to continue>>>")
            break

def about_the_author():
    clear()
    print("A highly motivated computer science student who likes programming.")
    input("\n\n\n\n\n\t<<<press ENTER to continue>>>")



main_menu()