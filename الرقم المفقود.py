def find_missing_number(n, numbers):
    # حساب مجموع الأرقام المتوقعة من 1 إلى n
    expected_sum = (n * (n + 1)) // 2

    # حساب مجموع الأرقام الموجودة في المصفوفة
    actual_sum = sum(numbers)

    # العدد المفقود هو الفرق بين المجموع المتوقع والمجموع الفعلي
    missing_number = expected_sum - actual_sum

    return missing_number


# اختبار الأمثلة
print(find_missing_number(5, [3, 5, 4, 2]))  # المخرجات: 1
print(find_missing_number(3, [1, 3]))  # المخرجات: 2
print(find_missing_number(7, [1, 7, 5, 4, 2, 6]))  # المخرجات: 3
print(find_missing_number(10, [2, 9, 8, 4, 1, 7, 10, 3, 6]))  # المخرجات: 5
