# Library Management System (Python – OOP Based)

## Project Overview
This project is a **Library Management System** developed in **Python** using **Object-Oriented Programming (OOP)** principles.  
It provides a command-line interface to manage books, library members, and borrowing operations, with persistent data storage using JSON files.

The project is designed to demonstrate **clean architecture, modular design, and real-world problem solving** using Python.

---

## Objectives
- Apply Object-Oriented Programming concepts in a real-world system
- Build a modular and maintainable Python application
- Implement file handling for persistent data storage
- Practice input validation and logical flow control
- Simulate core library operations such as borrowing and returning books

---

## Features
- Add new books to the library
- Register library members
- Search books by title, author, or ISBN
- Borrow books with due-date calculation
- Return borrowed books
- Enforce borrowing limits per member
- Persistent storage using JSON files
- Menu-driven command-line interface
- Unit testing for core modules

---

## Technologies Used
- **Programming Language:** Python 3
- **Concepts:** Object-Oriented Programming (OOP)
- **Data Storage:** JSON
- **Testing Framework:** PyTest
- **Version Control:** Git

---

## Project Structure
```

week5-library-system/
│
├── library_system/
│   ├── **init**.py
│   ├── book.py
│   ├── member.py
│   ├── library.py
│   ├── file_handler.py
│   └── main.py
│
├── data/
│   ├── books.json
│   ├── members.json
│   └── backup/
│
├── tests/
│   ├── test_book.py
│   ├── test_member.py
│   └── test_library.py
│
├── requirements.txt
├── README.md
└── .gitignore

````

---

## Module Description
- **book.py** – Defines the Book class and book-related operations
- **member.py** – Defines the Member class and borrowing limits
- **library.py** – Handles core library logic
- **file_handler.py** – Manages saving and loading data from JSON files
- **main.py** – Entry point providing a menu-driven interface
- **tests/** – Contains unit tests for major components

---

## How to Run the Project

### Prerequisites
- Python 3.x installed
- Git (optional)

### Steps
1. Clone the repository or download the project folder
2. Navigate to the project directory
   ```bash
   cd week5-library-system
````

3. Run the application

   ```bash
   python -m library_system.main
   ```

---

## Sample Usage

```
1. Add Book
2. Add Member
3. Borrow Book
4. Return Book
5. Search Book
6. Save & Exit
```

---

## Testing

To run unit tests:

```bash
pytest tests/
```

---

## Learning Outcomes

* Strong understanding of Python OOP concepts
* Experience in designing modular systems
* Practical knowledge of file handling and data persistence
* Writing clean, readable, and maintainable code
* Implementing real-world business logic

---

## Challenges Faced and Solutions

**Challenge:** Managing persistent data
**Solution:** Implemented JSON-based file handling using a dedicated module

**Challenge:** Preventing invalid borrowing
**Solution:** Added borrowing limits and availability checks

**Challenge:** Code scalability
**Solution:** Used modular design and separation of concerns

---

## Future Enhancements

* User authentication system
* Graphical User Interface (GUI)
* Database integration (MySQL/PostgreSQL)
* Fine calculation for late returns
* Book categories and advanced filters

---

## Quality Checklist

* Well-structured project folders
* Clean and commented Python code
* Professional documentation
* Sample usage included
* Unit test cases provided

---

## Conclusion

This project demonstrates a complete Python application using Object-Oriented Programming, suitable for academic evaluation and internship assessment.
It reflects best practices in code organization, documentation, and software design.

```
## 📤 Submission Notes

This project is **internship-ready** and meets all academic evaluation criteria for Week 5.

---

**Author:** Mehak Tewari
**Week:** 5 — Library Management System Project