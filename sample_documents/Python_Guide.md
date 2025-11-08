# Python Programming Guide for Beginners

## Introduction to Python

Python is a high-level, interpreted programming language known for its simplicity and readability. Created by Guido van Rossum and first released in 1991, Python has become one of the most popular programming languages in the world.

## Why Learn Python?

- **Easy to Learn**: Python has a simple syntax that mirrors natural language
- **Versatile**: Used in web development, data science, AI, automation, and more
- **Large Community**: Extensive libraries and strong community support
- **High Demand**: One of the most sought-after programming skills in the job market

## Basic Syntax

### Variables and Data Types

```python
# Variables (no declaration needed)
name = "John"
age = 25
height = 5.9
is_student = True

# Basic data types
integer_var = 42          # int
float_var = 3.14          # float
string_var = "Hello"      # str
boolean_var = True        # bool
```

### Operators

- Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical: `and`, `or`, `not`

## Control Structures

### If-Else Statements

```python
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```

### Loops

```python
# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
```

## Data Structures

### Lists
Lists are ordered, mutable collections.

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits[0] = "mango"
```

### Tuples
Tuples are ordered, immutable collections.

```python
coordinates = (10, 20)
```

### Dictionaries
Dictionaries store key-value pairs.

```python
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
```

### Sets
Sets are unordered collections of unique elements.

```python
unique_numbers = {1, 2, 3, 4, 5}
```

## Functions

Functions are reusable blocks of code.

```python
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

# Function call
result = add(5, 3)
```

## Object-Oriented Programming

### Classes and Objects

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"My name is {self.name} and I'm {self.age} years old"

# Create object
student1 = Student("Alice", 20)
print(student1.introduce())
```

### Inheritance

```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
```

## File Handling

### Reading Files

```python
# Read entire file
with open("file.txt", "r") as file:
    content = file.read()

# Read line by line
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())
```

### Writing Files

```python
with open("output.txt", "w") as file:
    file.write("Hello, World!")
```

## Exception Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("This always executes")
```

## Important Libraries

### Standard Library
- `math`: Mathematical functions
- `random`: Random number generation
- `datetime`: Date and time operations
- `os`: Operating system interface
- `json`: JSON parsing and generation

### Popular Third-Party Libraries
- `numpy`: Numerical computing
- `pandas`: Data analysis
- `matplotlib`: Data visualization
- `requests`: HTTP library
- `flask`/`django`: Web frameworks

## Best Practices

1. **Use meaningful variable names**: `student_count` instead of `sc`
2. **Follow PEP 8**: Python's style guide
3. **Write comments**: Explain complex logic
4. **Use functions**: Break code into smaller, reusable pieces
5. **Handle exceptions**: Anticipate and handle errors
6. **Test your code**: Write unit tests
7. **Use virtual environments**: Isolate project dependencies

## Common Patterns

### List Comprehension

```python
# Instead of:
squares = []
for i in range(10):
    squares.append(i**2)

# Use:
squares = [i**2 for i in range(10)]
```

### Lambda Functions

```python
# Anonymous functions
square = lambda x: x**2
result = square(5)
```

### Decorators

```python
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
```

## Practice Exercises

1. Write a function to check if a number is prime
2. Create a program to calculate factorial
3. Implement a simple calculator
4. Build a todo list application
5. Create a program to analyze text files

## Study Tips

- **Practice daily**: Consistency is key
- **Build projects**: Apply what you learn
- **Read code**: Study others' code
- **Debug actively**: Learn from errors
- **Join communities**: Participate in forums

## Resources for Further Learning

- Official Python Documentation: python.org
- Python Tutorial: w3schools.com/python
- Practice Problems: leetcode.com, hackerrank.com
- Books: "Python Crash Course", "Automate the Boring Stuff"
- Video Courses: Coursera, Udemy, YouTube

---

**Remember**: The best way to learn programming is by doing. Start with small projects and gradually increase complexity!
