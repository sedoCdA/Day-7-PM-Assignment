# Part D: AI Type Conversion Matrix — Critical Evaluation

## Prompt Used

> "Generate a Python type conversion matrix showing what happens when you
> convert between int, float, str, bool, list, and tuple — include edge
> cases and potential errors."

---

## AI-Generated Conversion Matrix (Tested & Annotated)

| From → To | `int()` | `float()` | `str()` | `bool()` | `list()` | `tuple()` |
|-----------|---------|-----------|---------|----------|----------|-----------|
| `int`     | —       | ✅ `float(3)` → `3.0` | ✅ `str(3)` → `'3'` | ✅ `bool(0)` → `False` | ❌ TypeError | ❌ TypeError |
| `float`   | ✅ truncates `int(3.9)` → `3` | — | ✅ `str(3.9)` → `'3.9'` | ✅ `bool(0.0)` → `False` | ❌ TypeError | ❌ TypeError |
| `str`     | ✅ if numeric `int('3')` → `3` | ✅ `float('3.5')` → `3.5` | — | ✅ empty=False, else True | ✅ `list('hi')` → `['h','i']` | ✅ `tuple('hi')` → `('h','i')` |
| `bool`    | ✅ `int(True)` → `1` | ✅ `float(True)` → `1.0` | ✅ `str(True)` → `'True'` | — | ❌ TypeError | ❌ TypeError |
| `list`    | ❌ TypeError | ❌ TypeError | ✅ `str([1,2])` → `'[1, 2]'` | ✅ empty=False | — | ✅ `tuple([1,2])` → `(1,2)` |
| `tuple`   | ❌ TypeError | ❌ TypeError | ✅ `str((1,2))` → `'(1, 2)'` | ✅ empty=False | ✅ `list((1,2))` → `[1,2]` | — |

---

## Tested in Python — Key Results
```python
# int conversions
print(int(3.99))        # 3  — truncates, does NOT round
print(int("42"))        # 42 — works
print(int("3.5"))       # ValueError — cannot convert float string directly
print(int(True))        # 1
print(int(False))       # 0

# float conversions
print(float("3.14"))    # 3.14
print(float("inf"))     # inf — valid!
print(float(True))      # 1.0

# str conversions
print(str(None))        # 'None' — not an error
print(str([1, 2, 3]))   # '[1, 2, 3]'

# bool conversions
print(bool(0))          # False
print(bool(""))         # False
print(bool("False"))    # True  ← common mistake!
print(bool([]))         # False
print(bool([0]))        # True  ← list with content, even if 0

# list/tuple
print(list("abc"))      # ['a', 'b', 'c']
print(tuple(range(3)))  # (0, 1, 2)
```

---

## Critical Evaluation (150–200 words)

The AI-generated conversion matrix was well-structured and covered the
most common conversions accurately. The layout as a table made it easy to
scan and the inclusion of TypeError warnings was helpful for avoiding
runtime crashes.

What the AI got right: it correctly flagged that `int()` truncates rather
than rounds, that `bool("False")` evaluates to `True` (a classic beginner
trap), and that converting lists or tuples to `int` or `float` raises
a TypeError. These are the errors beginners hit most often.

What was missing or inaccurate: the AI did not mention that
`int("3.5")` raises a ValueError — you cannot pass a decimal string
directly to `int()`, you must go through `float` first:
`int(float("3.5"))`. It also missed `float("inf")` and `float("nan")`
which are valid conversions with surprising results. The edge case of
`bool([0])` returning `True` was not highlighted — beginners commonly
assume a list containing `0` would be falsy.

What I would add: a dedicated column for `None` conversions, and explicit
notes that `str()` never raises an error on any type — it is always safe
to call. Overall the AI output was a solid 80% complete starting point
that needed manual testing to uncover the remaining edge cases.
