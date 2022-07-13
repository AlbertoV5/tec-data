|                       |
|---------------------- |
| [<<Home](../readme.md) |

These notes are taken during the class.


# Introduction

```shell
python --version
```

    Python 3.7.6

1.  Why a programming language?
2.  Why Python?
3.  Why Data?

We will use Python for everything. From data collection, data cleaning to API connections, databases, ML, data visualization, etc.

Python is easy to distribute, it can be compiled to use with other languages and it&rsquo;s easy to work with.

Recommendations:

1.  Take a lot of notes
2.  Check on Slack
3.  Put more hours into studying
4.  Make diagrams
5.  Look for extra resources


# Terminal commands

List of useful terminal commands:

```shell
# See files in directory:
ls
# See all files (including hidden) in directory:
ls -a
# Move to another directory:
cd .
# Create a new directory.
mkdir example
# Create an empty file.
touch ./example/example.py
# Open a finder/explorer window in current directory.
open .
# Edit a file:
open example/example.py
# Edit file with editor:
code example/example.py
# Clear terminal clutter:
clear
```


# Python


## Variables

Declaring variables.

```python
title = "doctor"
year = 2022
expert = True
print("Carlos is a " + title)
print("Current year is " + str(year))
print("Is Galo an expert? " + str(expert))
print(f"Current year is {year}, Carlos is a {title}. Is Galo an expert? {expert}")
```

    Carlos is a doctor
    Current year is 2022
    Is Galo an expert? True
    Current year is 2022, Carlos is a doctor. Is Galo an expert? True


## Variables Activity

```python
# Create a variable called 'name' that holds a string
name = "Alberto"
# Create a variable called 'country' that holds a string
country = "Mexico"
# Create a variable called 'age' that holds an integer
age = 27
# Create a variable called 'hourly_wage' that holds an integer
hourly_wage = 15
# Calculate the daily wage for the user
daily_wage = hourly_wage * 8
# Create a variable called 'satisfied' that holds a boolean
satisfied = True
# Print out "Hello <name>!"
print(f"Hello {name}!")
# Print out what country the user entered
print(f"{country}")
# Print out the user's age
print(f"{age}")
# With an f-string, print out the daily wage that was calculated
print(f"${daily_wage}")
# With an f-string, print out whether the users were satisfied
print(f"{satisfied}")
```

    Hello Alberto!
    Mexico
    27
    $120
    True


# Data Structures


## Lists

Arrays, a way to organize data in a contiguous place. Lists can hold multiple data types, strings, integers, boolean, etc. Lists in python are zero-based (index starts at zero).

```python
# Creating a list
my_list = ["Jacob", 25, "Ahmed", 80]
print(f"My original list: {my_list}")
# Adding elements with =my_list.append()= or =my_list[]=
my_list.append("Matt")
my_list[3] = 85
print(f"My list with Matt: {my_list}")
# Removing elements in a list with my_list.pop()
my_list.pop(2)
print(f"My list without index 2: {my_list}")
# Getting index of an element with my_list.index()
jacob_index = my_list.index("Jacob")
print(f"Jacob's index: {jacob_index}")
# You can override elements with elements of differnt types
my_list[0] = True
print(f"My list's new index 0: {my_list[0]}")
# Get the length of a list with len(my_list)
print(f"Length of my list: {len(my_list)}")
```

    My original list: ['Jacob', 25, 'Ahmed', 80]
    My list with Matt: ['Jacob', 25, 'Ahmed', 85, 'Matt']
    My list without index 2: ['Jacob', 25, 85, 'Matt']
    Jacob's index: 0
    My list's new index 0: True
    Length of my list: 4


## Tuples

Tuples are immutable lists (you can&rsquo;t modify them).

```python
my_tuple = (0, 1, 2, 3, 4)
print(f"my_tuple is {my_tuple}")
# unpacking tuples
new_tuple = (my_tuple[0], my_tuple[3])
print(f"new_tuple is {new_tuple}")
```

    my_tuple is (0, 1, 2, 3, 4)
    new_tuple is (0, 3)


## Activity - Groceries

```python
# Create a Python list to store your grocery list
groceries = ["Milk", "Jelly", "Orange Juice","Peanut Butter"]
# Print the grocery list
print(groceries)
# Change "Peanut Butter" to "Almond Butter" and print out the updated list
groceries[groceries.index("Peanut Butter")] = "Almond Butter"
print(groceries)
# Remove "Jelly" from grocery list and print out the updated list
groceries.remove("Jelly")
print(groceries)
# Add "Coffee" to grocery list and print the updated list
groceries.append("Coffee")
print(groceries)
```

    ['Milk', 'Jelly', 'Orange Juice', 'Peanut Butter']
    ['Milk', 'Jelly', 'Orange Juice', 'Almond Butter']
    ['Milk', 'Orange Juice', 'Almond Butter']
    ['Milk', 'Orange Juice', 'Almond Butter', 'Coffee']


## Dictionaries

A dictionary is a key, value pair collection of data.

The key must be a string (or an immutable variable) and the value can be whatever. Example:

```python
actors_list = ["Tom", "Angelina", "Kristen", "Denzel"]
actors_dict = {"name": "Tom", "lastname": "Cruise"}
# Accessing the dictionary:
print(f'{actors_dict["name"]}, {actors_dict["lastname"]}')
```

    Tom, Cruise

A dictionary with many values.

```python
another_actor = {
    "name": "Angelina Jolie",
    "genre": "Action",
    "married": False,
    "best_movies": ["Tomb Raider","Malefica"],
    "age": 50,
}
print(f"{another_actor['name']}")
```

    Angelina Jolie


## Activity - Pet Hobbies

1.  Create a dictionary to store the following:
    -   Your pet&rsquo;s name
    -   Your pet&rsquo;s age
    -   A list of a few of your pet&rsquo;s hobbies
    -   A dictionary of a few times you wake up during the week

2.  Print out the following:
    -   Your pet&rsquo;s name and age.
    -   How many hobbies your pet has.
    -   What your pet&rsquo;s favorite hobby is.
    -   What time your pet wakes on one of the days of the week.

```python
pet_info = {
    "name": "Zuri",
    "age": "16",
    "hobbies": ["sleeping", "eating", "peeing"],
    "wake_up": {
        "Mon": 7,
        "Friday": 11,
        "Saturday": 7,
        "Sunday": 5
    }
}
print(f"Hello I am {pet_info['name']} and I am {pet_info['age']} years old.")
print(f"I have {len(pet_info['hobbies'])} hobbies: {pet_info['hobbies']}.")
print(f"My favorite hobby is {pet_info['hobbies'][0]}.")
print(f"My wake up time on Monday is {pet_info['wake_up']['Mon']}:00 a.m.")
```

    Hello I am Zuri and I am 16 years old.
    I have 3 hobbies: ['sleeping', 'eating', 'peeing'].
    My favorite hobby is sleeping.
    My wake up time on Monday is 7:00 a.m.


# Office hours


## When to use [] or {} or ()?

-   [] for accessing a dictionary key or a list index.
-   {} for creating a dictionary or in f-strings.
-   () for using a function.

```python
# creating and accessing lists
my_list = ["a", "b", "c", "d"]
print(my_list[0])
# creating and accessing dictionaries
my_dictionary = {"r":0.0, "g": 0.0, "b": 1.0, "a": 1.0}
print(my_dictionary["a"])
# using function to get info of data structures/variables
my_list_length = len(my_list)
print(my_list_length)
```

    a
    1.0
    4


## What is Anaconda, IDLE, VS Code?

They are different ways to work with python code. Anaconda is an environment manager and package manager, IDLE is an editor and VS Code is a very powerful editor that can become an Integrated Development Environment when using extensions.


## Can we use `my_list.index()` instead of accessing it with `[i]`?

Yes.


## Can we work with Python 3.10 or other version that is not 3.7?

We can work with any version of Python out of the box but the problems raise whenever we work with libraries. Some versions have very different syntax like [f-strings in version 3.6.](https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep498)


## How to know if we have Python installed?

There is no &ldquo;Python app&rdquo;. You can know what version you have installed using: `python --version` or `py --version` in the terminal.


## Do we need to change directory for executing python code?

Depends if we are in a workspace. A workspace is a folder with all the files we are using in a project/app/library, etc.

-   If we are in a workspace, VS Code will open a terminal in that workspace&rsquo;s folder.
-   If we are just editing single files, VS Code will open a terminal in the home directory.

If we use `right-click=>run python file from terminal` in VS Code it will adapt to the location of the file. For example, running a file directly in the working directory:

```shell
python HelloVariableWorld.py
```

Running a file from another directory:

```shell
python /Users/albertovaldez/tec-data/week-3/lesson-1/3-1-Student-Resources/03-Stu_HelloVariableWorld/Unsolved/HelloVariableWorld.py
```

Credit to Naomi for the Office Hours responses.