from typing import List
def sum_numbers(num: int, s: str) -> int:
    if s not in ["زوجي", "فردي"]:
        raise ValueError("يجب أن يكون النص 'زوجي' أو 'فردي'")

    if s == "زوجي":
        return sum(i for i in range(2, num+1, 2))
    else:
        return sum(i for i in range(1, num+1, 2))

num = 5
s = 'زوجي'
print(sum_numbers(num, s))

num = 10
s = 'زوجي'
print(sum_numbers(num, s))

num = 15
s = 'فردي'
print(sum_numbers(num, s))

num = 7
s = 'فردي'
print(sum_numbers(num, s))

    # write your code here ^_^



