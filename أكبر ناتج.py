from typing import List


def expression(num1: int, num2: int, num3: int) -> int:
    # Generate all possible expressions
    expressions = [
        num1 + num2 + num3,
        num1 * num2 * num3,
        num1 * (num2 + num3),
        (num1 + num2) * num3
    ]

    # Return the maximum value
    return max(expressions)


# Testing the function with provided test cases
tests = [
    (1, 2, 3),
    (1, 3, 2),
    (3, 4, 2),
    (5, 2, 1)
]

for i, test in enumerate(tests, start=1):
    num1, num2, num3 = test
    print(f"Test {i}")
    print("Inputs:")
    print(f"num1 = {num1}")
    print(f"num2 = {num2}")
    print(f"num3 = {num3}")
    print("Output:")
    print(expression(num1, num2, num3))
    print()
