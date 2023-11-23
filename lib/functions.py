#!/usr/bin/env python3

def greet_programmer():
    pass
    print("Hello, programmer!")
greet_programmer()
def greet(name):
    pass
    print(f"Hello, {name}!")
greet("Khalifa")
def greet_with_default(name="programmer"):
    pass
    print(f"Hello, {name}!")
greet_with_default()
def add(num1: int, num2: int) -> int:
    result = num1 + num2
    return result
add(45, 55)    
def halve(number: float)-> float:
    result = number / 2
    return result
halve(99.0)    