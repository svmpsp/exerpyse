# Exerpyse - Learn Python by Exercise

Learn Python by completing a series of short programming exercises with instant feedback!

---

## What you will learn

- **Exercise 1** — Basic arithmetic: writing a function that adds two numbers
- **Exercise 2** — String manipulation: detecting whether a word is a palindrome

More exercises are planned covering loops, lists, dictionaries, and more.

---

## Installation

```bash
python3 -m pip install exerpyse
```

---

## Getting started

Follow these steps to run your first exercise session:

**1. Copy the exercises folder to your working directory**

```bash
cp -r $(python3 -c "import exerpyse; import os; print(os.path.dirname(exerpyse.__file__))")/include/exercises ./exerpyses
```

Or download the folder manually from the repository and place it in your project.

**2. Open an exercise file and write your solution**

Each file contains a function stub with a docstring describing the task:

```python
# exerpyses/ex01.py

"""Exercise 1: summing two numbers

Complete the function below so that it returns
the sum of its parameters.
"""


def do_things(param_1: int, param_2: int) -> int:
    # Add your code here

    return 42
```

Replace the placeholder body with your solution:

```python
def do_things(param_1: int, param_2: int) -> int:
    return param_1 + param_2
```

**3. Run the checker**

```bash
exerpyse start
```

You will see immediate pass/fail feedback for each exercise in your folder. Fix any failures and re-run until everything is green.

---

## Course structure

| Exercise | File | Python concept |
|----------|------|----------------|
| 1 | `ex01.py` | Arithmetic operators, function return values |
| 2 | `ex02.py` | String indexing, boolean return values |

---

## Tips for beginners

- **Read the docstring first.** Every exercise file starts with a description of exactly what the function should do. Understanding the goal before writing any code saves time.
- **Run often.** You do not have to solve the whole exercise before running `exerpyse start`. Run it after every small change to see whether you are moving in the right direction.
- **Keep it simple.** Python has built-in operators and functions for most common tasks. Before writing a loop, check whether a simpler expression works.
- **Errors are normal.** A failing test is not a problem — it is information. Read the output carefully to understand what your function returned versus what was expected.
- **One exercise at a time.** Work through the exercises in order. Later exercises sometimes build on concepts introduced earlier.

---

©️ Sivam Pasupathipillai. All rights reserved.
