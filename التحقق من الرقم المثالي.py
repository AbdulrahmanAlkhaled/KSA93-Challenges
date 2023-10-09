def perfect_Number_check(num: int) -> bool:
    if num <= 0:
        return False

    # Initialize the sum of proper divisors
    divisors_sum = 0

    # Iterate through numbers starting from 1 up to num/2
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisors_sum += i

    # Check if the sum of divisors equals the original number
    return divisors_sum == num

# Testing the function with the provided test cases
print(perfect_Number_check(6))  # Expected output: True
print(perfect_Number_check(28))  # Expected output: True
print(perfect_Number_check(12))  # Expected output: False
print(perfect_Number_check(14))  # Expected output: False
