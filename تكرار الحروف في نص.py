from typing import List

def character_count(word: str) -> str:
    # تحويل النص إلى حروف صغيرة للتماثل
    word = word.lower()

    # قائمة لتخزين الحروف وعدد تكرار كل حرف
    char_counts = []

    # حساب عدد تكرار كل حرف
    for char in sorted(set(word)):
        count = word.count(char)
        char_counts.append(f'{char}{count}')

    # الانضمام للناتج في ترتيب أبجدي
    result = ''.join(char_counts)

    return result

# اختبارات
test_cases = ['aabbbcccc', 'abc', 'Hello', 'aabbcc']

for word in test_cases:
    print(f'Input: {word}')
    print(f'Output: {character_count(word)}')

    # write your code here ^_^
