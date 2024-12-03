# Homework 1

## Overview
Exercises on:
1. Binary Search Implementation (iterative and recursive)
2. Text Processing Operations
3. Number Theory Functions

## Project Structure
```
homework_1/
├── README.md
├── requirements.txt
├── main.py
├── tests/
│   ├── __init__.py
│   ├── test_search.py
│   ├── test_text_ops.py
│   └── test_number_ops.py
└── src/
    ├── __init__.py
    └── homework/
        ├── __init__.py
        ├── search.py
        ├── text_ops.py
        └── number_ops.py
```

## Setup Instructions

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Exercise Descriptions

### Exercise 1: Binary Search Implementation
Implement both iterative and recursive versions of binary search in `search.py`:

Requirements:
- Add print statements to show search progress
- Handle edge cases (empty list, target not found)
- Compare recursive vs iterative approach
- Include input validation

### Exercise 2: Text Processing
Create text processing functions in `text_ops.py`:

Requirements:
- Remove punctuation before processing
- Convert text to lowercase for word counting
- Handle multiple spaces and newlines
- Use list/dictionary comprehensions

### Exercise 3: Number Theory Functions
Implement number theory functions in `number_ops.py`:

Requirements:
- Use recursive approach for fibonacci and sum_of_digits
- Handle negative numbers
- Include input validation

## Test Files

## Running Tests
To run specific test files:
```bash
pytest tests/test_search.py
pytest tests/test_text_ops.py
pytest tests/test_number_ops.py
```
