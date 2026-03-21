# python-100-days-challenge
A collection of my daily Python practice, including concepts, exercises, and small projects as part of the 100 Days of Python challenge.





🚀 Day 27 of #100DaysOfPython 🐍

Today I built a KBC (Kaun Banega Crorepati) Game in Python 🎮

This was one of the most exciting exercises so far where I created a quiz system that asks questions, checks answers, and rewards money based on performance 💰

📚 Concepts used:
🔹 Lists to store questions and answers
🔹 Conditional statements
🔹 User input handling
🔹 Basic game logic building


This exercise helped me understand how to build interactive programs and game logic using Python. 


-----


🚀 Day 28 of #100DaysOfPython 🐍

Today I learned about f-strings (Formatted Strings) in Python.

f-strings are a modern and easy way to insert variables directly inside strings using "{}". They make code more readable and cleaner compared to older methods like concatenation or ".format()"

📚 Concepts I practiced:

🔹 Using "f" before strings
🔹 Embedding variables inside "{}"
🔹 Performing calculations inside strings
🔹 Formatting output easily

💻 Example Code:

name = "Taylor"
age = 20

# Using f-string
print(f"My name is {name} and I am {age} years old.")

# Expressions inside f-string
a = 10
b = 5
print(f"Sum of {a} and {b} is {a + b}")

🧠 Output 

My name is Taylor and I am 20 years old.
Sum of 10 and 5 is 15

✨ f-strings make Python code simpler, faster, and more readable.


------


🚀 Day 29 of #100DaysOfPython 🐍

Today I learned about writing clean and readable Python code, which is just as important as making the code work.

📚 Topics covered:
🔹 Docstrings – Used to document functions and make code easier to understand
🔹 PEP 8 – The official style guide for writing clean and consistent Python code
🔹 Zen of Python – A collection of guiding principles that emphasize simplicity, readability, and clarity in programming

💡 One of my favorite lines from the Zen of Python:
“Simple is better than complex.”

These concepts helped me understand that good programming is not just about solving problems, but also about writing code that others (and future me) can easily read and maintain.


------


🚀 Day 30 – Recursion in Python

On Day 30 of my Python learning journey, I explored recursion, a programming technique where a function calls itself to solve a problem. Recursion is especially useful for problems that can be broken down into smaller, similar subproblems.


🧠 What I Learned

What recursion is and how it works

Base case and recursive case

How recursion stops to prevent infinite calls

Simple examples like factorial and Fibonacci series



---

🔁 What is Recursion?

Recursion is when a function calls itself repeatedly until a stopping condition (base case) is met.

def example():
    example()  # function calling itself

Without a base case, recursion would run forever and cause an error.


---

🧮 Example 1: Factorial Using Recursion

def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    return n * factorial(n - 1)  # recursive call

print(factorial(5))

Output:

120


---

🔢 Example 2: Fibonacci Series Using Recursion

def fibonacci(n):
    if n <= 1:  # base case
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))

Output:

8


⚙️ Key Concepts

Base Case: Stops the recursion

Recursive Case: Function calling itself

Stack Memory: Each recursive call is stored in memory until the base case is reached



---

📂 Files in This Folder

recursion.py – Contains basic recursion examples like factorial and Fibonacci
