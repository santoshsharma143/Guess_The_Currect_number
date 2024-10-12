Number Guessing Game

**Purpose:**

This Python code implements a simple number guessing game. The user tries to guess a randomly generated number between 1 and 100. The program provides hints (higher or lower) until the correct guess is made.

**How to Use:**

**Run the code:**
Execute the Python script in your preferred environment (e.g., terminal, IDE).

**Guess the number:**
The program will prompt you to enter a number between 1 and 100.

**Receive feedback:**
Based on your guess, the program will display a message indicating whether the number is higher or lower than the target.

**Continue guessing:**
Keep entering numbers until you correctly guess the random number.
Code Explanation:

**Initialization:**

**import random:**
Imports the random module to generate a random number.

**num = random.randint(1,100):**
Generates a random integer between 1 and 100 and stores it in the num variable.

**a = -1:**
Initializes the a variable to a value that is not the target number, ensuring the loop will run at least once.

**attempts = 0:**
Initializes the attempts variable to keep track of the number of guesses.

**Guessing loop:**
while (a != num):: The loop continues as long as the user's guess (a) is not equal to the target number (num).

**a = int(input("Guess the number : ")):**
Prompts the user to enter a guess and converts it to an integer.

**if (a < num):**
If the guess is less than the target number, prints "Think more higher number" and increments the attempts variable.

**else:** 
If the guess is greater than the target number, prints "Think more lower number" and increments the attempts variable.
Final message:

**print(f"You Guessed the {num} in {attemps} attemps"):** Prints a message indicating the guessed number and the number of attempts taken.

**Additional Notes:**

You can customize the range of numbers by modifying the arguments to random.randint().
Consider adding error handling to validate user input (e.g., ensuring the input is a valid integer within the specified range).
For a more challenging version, you could implement a difficulty level that adjusts the range of numbers based on the user's choice.
