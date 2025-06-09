import math
import time
import os
import random

#version #
version = "0.1.2"

#set the window title
os.system('title Python CHANCE! v' + str(version))

ram1 = 0
ram2 = 0
ram3 = 0
ram4 = 0
ram5 = 0

start_time = 0

inp = 0
args = []

def clear():
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')



while True:

    # Get the current time
    start_time = time.time()
    
    clear()
    print("Python CHANCE! v" + str(version))
    print("Current time: " + time.strftime("%H:%M:%S", time.localtime()))
    print("")
    print("Select an option from below, using it's corresponding number:")
    print("==========================")
    print("1 ... Random Number - Custom Range")
    print("2 ... Higher/Lower game - Range 1-1000")
    print("3 ... Higher/Lower game - Custom Range")
    print("4 ... Higher/Lower - Automatic with Custom Range")
    print("5 ... Roulette Spinner - Number and Color")
    print("6 ... Random Number Series - Custom Range + Count")
    print("7 ... Random String - Custom Length and Characters")
    print("8 ... Exit")
    print("==========================")

    # Get user input
    inp = input("Enter your choice: ")

    # Check if input is a number
    if type(inp) == int:
        if inp == 1:
            # Random Number - Custom Range
            clear()
            ram1 = input("Enter the minimum number: ")
            ram2 = input("Enter the maximum number: ")
            if type(ram1) == type(ram2) and type(ram1) == int:
                ram1 = int(ram1)
                ram2 = int(ram2)
                print("Result: " + str(random.randint(ram1, ram2)))
                ram3 = input("Press Enter to continue...")
                ram3 = 0
            else:
                print("Invalid input. Please enter numbers.")
    else:
        print("Invalid input. Please enter a number.")
        time.sleep(2)
        continue
