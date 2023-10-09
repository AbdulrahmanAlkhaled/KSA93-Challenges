from typing import List

def int_to_roman(num: int) -> str:
    # قائمة بالأرقام الرومانية وقيمها المقابلة
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    result = ''
    for value, numeral in roman_numerals.items():
        while num >= value:
            result += numeral
            num -= value

    return result

# الاختبارات المذكورة في الوصف
print(int_to_roman(1))  # المخرج المتوقع: 'I'
print(int_to_roman(2))  # المخرج المتوقع: 'II'
print(int_to_roman(6))  # المخرج المتوقع: 'VI'
print(int_to_roman(23))  # المخرج المتوقع: 'XXIII'
