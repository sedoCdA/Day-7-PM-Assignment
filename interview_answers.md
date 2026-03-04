# Part C: Interview Ready

---

## Q1 — Data Types Deep Dive: Predict the Output
```python
print(type(True))
```
**Predicted:** `<class 'bool'>`
**Explanation:** `True` is of type `bool` in Python.

---
```python
print(isinstance(True, int))
```
**Predicted:** `True`
**Explanation:** In Python, `bool` is a subclass of `int`.
`True` is treated as `1` and `False` as `0`, so `isinstance(True, int)` returns `True`.

---
```python
print(True + True + False)
```
**Predicted:** `2`
**Explanation:** `True` = 1, `False` = 0, so `1 + 1 + 0 = 2`.

---
```python
print(int(3.99))
```
**Predicted:** `3`
**Explanation:** `int()` truncates (does NOT round), so 3.99 becomes 3.

---
```python
print(bool("False"))
```
**Predicted:** `True`
**Explanation:** Any non-empty string is truthy in Python — even the string
`"False"`. Only an empty string `""` is falsy.

---
```python
print(bool(""))
```
**Predicted:** `False`
**Explanation:** An empty string has no content so Python treats it as falsy.

---
```python
print(0.1 + 0.2 == 0.3)
```
**Predicted:** `False`
**Explanation:** Floating-point numbers cannot be represented exactly in
binary. `0.1 + 0.2` actually equals `0.30000000000000004` in memory, not
exactly `0.3`. This is a well-known IEEE 754 floating-point precision issue.
Use `math.isclose(0.1 + 0.2, 0.3)` for reliable float comparison.

---
```python
print("5" + "3")
```
**Predicted:** `"53"`
**Explanation:** When `+` is used on two strings, it concatenates them —
it does not add numerically.

---
```python
print(5 + 3)
```
**Predicted:** `8`
**Explanation:** When `+` is used on two integers, it performs arithmetic addition.

---

## Q2 — Type Analyzer Function
```python
"""Type analyzer module."""


def analyze_value(value):
    """
    Analyze a value and return its type, truthiness, and length.

    Args:
        value: Any Python value to analyze.

    Returns:
        str: Formatted string with value details.
    """
    val_type = type(value).__name__
    truthy = bool(value)

    try:
        length = len(value)
    except TypeError:
        length = "N/A"

    return f"Value: {value} | Type: {val_type} | Truthy: {truthy} | Length: {length}"


# Test cases
print(analyze_value(42))
print(analyze_value(""))
print(analyze_value([1, 2, 3]))
print(analyze_value(0))
print(analyze_value({"key": "val"}))
print(analyze_value(None))
print(analyze_value((1, 2)))
```

**Output:**
```
Value: 42 | Type: int | Truthy: True | Length: N/A
Value:  | Type: str | Truthy: False | Length: 0
Value: [1, 2, 3] | Type: list | Truthy: True | Length: 3
Value: 0 | Type: int | Truthy: False | Length: N/A
Value: {'key': 'val'} | Type: dict | Truthy: True | Length: 1
Value: None | Type: NoneType | Truthy: False | Length: N/A
Value: (1, 2) | Type: tuple | Truthy: True | Length: 2
```

---

## Q3 — Debug: Find & Fix 4 Bugs

### Original Buggy Code:
```python
name = input("Name: ")
age = input("Age: ")

if age >= 18:
    status = "Adult"
else:
    status = "Minor"

print(f"name is {age} years old and is a {status}")
print(f"In 5 years: {age + 5}")

score = 85.5
print(f"Score: {score:.0}")
```

### The 4 Bugs:

**Bug 1:** `age >= 18` — `input()` always returns a `str`.
You cannot compare a string to an integer with `>=`.
**Fix:** `age = int(input("Age: "))`

**Bug 2:** `f"name is {age} years old"` — The variable `name` is used as
a literal word instead of the variable. Should be `{name}`.
**Fix:** `print(f"{name} is {age} years old and is a {status}")`

**Bug 3:** `{age + 5}` — Even after fixing Bug 1 with `int()`, if you left
`age` as a string this would crash. After fix 1 this works, but the original
code has a `TypeError` here.
**Fix:** Depends on Bug 1 fix — once `age` is `int`, `age + 5` works.

**Bug 4:** `{score:.0}` — Invalid f-string format specifier. To show zero
decimal places you must write `:.0f` (the `f` for float is required).
**Fix:** `print(f"Score: {score:.0f}")`

### Corrected Code:
```python
"""Corrected age and score script."""

name = input("Name: ")
age = int(input("Age: "))

if age >= 18:
    status = "Adult"
else:
    status = "Minor"

print(f"{name} is {age} years old and is a {status}")
print(f"In 5 years: {age + 5}")

score = 85.5
print(f"Score: {score:.0f}")
```
