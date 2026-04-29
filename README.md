# Simple-Login-System
A simple login system built with python
# Simple Login System (Python)
A basic command-line login system built with Python.
This program allows users to enter a username and password, validates the credentials, and limits the number of login attempts.

## Features

* Username and password authentication
* Maximum attempt limit (3 tries)
* Clear feedback for incorrect inputs
* Tracks number of login attempts
* Blocks access after too many failed attempts

## What I Learned

* Using "while" loops for repeated user interaction
* Applying conditional statements ("if", "elif", "else")
* Working with logical operators ("and")
* Controlling program flow with "break" and loop conditions
* Building simple authentication logic

## How It Works

1. The user is prompted to enter a username and password
2. The program checks if the credentials match stored values
3. If incorrect, the user is informed and can try again
4. After 3 failed attempts, access is denied
5. If correct, login is successful and the program ends

## Note

This is a beginner-level project and stores credentials directly in the code.
In real-world applications, passwords should be securely hashed and stored in a database.

## Future Improvements

* Hide password input using "getpass"
* Store user credentials in a file or database
* Add user registration system
* Implement account lockout timer
* Build a graphical user interface (GUI)

## Author

Olamide Ibikunle Joshua

## Acknowledgment

This project is part of my Python learning journey and practice with problem-solving and program logic.
