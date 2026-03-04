"""
Type Analyzer — Part C Q2.

Analyzes any Python value and returns its type, truthiness, and length.
"""


def analyze_value(value):
    """
    Analyze a value and return its type, truthiness, and length.

    Args:
        value: Any Python value to analyze.

    Returns:
        str: A formatted string summarizing the value's properties.
    """
    val_type = type(value).__name__
    truthy = bool(value)

    try:
        length = len(value)
    except TypeError:
        length = "N/A"

    return f"Value: {value} | Type: {val_type} | Truthy: {truthy} | Length: {length}"


if __name__ == "__main__":
    test_values = [42, "", [1, 2, 3], 0, 3.14, None, {"a": 1}, (1, 2), True, "hello"]
    print("=== Type Analyzer Results ===")
    for val in test_values:
        print(analyze_value(val))
