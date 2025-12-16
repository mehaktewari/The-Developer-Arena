# Student Grade Calculator — Week 2 Internship Task

## Overview
The **Student Grade Calculator** is a Python-based application developed as part of **Week 2 of the internship program**.  
It demonstrates practical use of **control flow, data structures, loops, functions, and error handling**.

The program processes marks of multiple students, assigns grades with personalized comments, and calculates class-level statistics.

---

## Objectives
- Apply conditional logic using if/elif/else
- Store and process data using lists
- Use loops for repetitive tasks
- Handle invalid inputs gracefully
- Build a structured, real-world Python program

---

## Technologies Used
- Python 3
- Visual Studio Code
- Command Line Interface (CLI)

---

## Project Structure
```

week2-grade-calculator/
│── grade_calculator.py
│── README.md
│── test_students.txt
│── results_sample.txt
└── .gitignore

````

---

## Features
- Processes multiple students
- Grade calculation with comments
- Input validation using loops and try-except
- Class statistics (average, highest, lowest)
- Clean tabular output
- Modular code using functions

---

## Grading System
| Grade | Marks Range | Description |
|------|------------|-------------|
| A | 90–100 | Excellent |
| B | 80–89 | Very Good |
| C | 70–79 | Good |
| D | 60–69 | Needs Improvement |
| F | 0–59 | Failed |

---

## How to Run
```bash
cd week2-grade-calculator
python grade_calculator.py
````

To test with sample input:

```bash
python grade_calculator.py < test_students.txt
```

---

## Sample Output

```
==================================================
      STUDENT GRADE CALCULATOR
==================================================

Enter number of students: 2

John Smith | 88.3 | B | Very Good!
Sarah Johnson | 81.3 | B | Very Good!
```

---

## What I Learned

* Conditional logic and decision making
* Lists and list comprehensions
* for and while loops
* Error handling with try-except
* Writing modular and readable Python code

---

## Challenges & Solutions

**Invalid user input**
→ Solved using while loops and try-except blocks

**Formatting output**
→ Solved using f-strings with fixed widths

---

## Author

**Mehak Tewari**
Python Internship — Week 2

---

✔ Week 2 Internship Task Completed Successfully

````
