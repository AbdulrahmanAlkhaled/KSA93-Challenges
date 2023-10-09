from typing import List

def isInterleave(A: str, B: str, C: str) -> bool:
    len_a, len_b, len_c = len(A), len(B), len(C)

    # إذا كان إجمالي طول C لا يتساوى مع إجمالي طول A و B، فهو غير صالح
    if len_c != len_a + len_b:
        return False

    # المؤشرات لتتبع الحروف في A و B
    pointer_a, pointer_b = 0, 0

    # يمر عبر الحروف في C
    for char in C:
        if pointer_a < len_a and A[pointer_a] == char:
            pointer_a += 1
        elif pointer_b < len_b and B[pointer_b] == char:
            pointer_b += 1
        else:
            # إذا لم يكن الحرف في A أو B، فالترتيب غير صالح
            return False

    return True


# Be sure to test the function with the provided test cases
print(isInterleave('wysn', 'showus', 'shwysowuns'))  # True
print(isInterleave('hsbxib', 'ywssg', 'hsywbxsisgb'))  # True
print(isInterleave('zh2g', 'wts', 'shwt2gs'))  # False
print(isInterleave('hsyhag', '2b12', 'hsy2bhag1'))  # False
