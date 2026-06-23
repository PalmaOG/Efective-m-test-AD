def missing_number(nums):
    n = len(nums) + 1
    total = n * (n + 1) // 2
    return total - sum(nums)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11]
print(missing_number(nums))
#Сложность O(n)