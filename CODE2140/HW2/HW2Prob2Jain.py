def sum_product(nums, in_mode = 0):
    sum_or_product = 0
    min_or_max = nums[0]
    if in_mode == 0:
        for num in nums:
            if (num < min_or_max):
                min_or_max = num
            sum_or_product += num
    else:
        sum_or_product = 1
        for num in nums:
            if (num > min_or_max):
                min_or_max = num
            sum_or_product *= num
    return (sum_or_product, min_or_max)

print(sum_product([1,2,3,4,5]))
print(sum_product([36, 23, 47, 35, 90, 100, 87], 1))
print(sum_product([2, 25, 1, -1], 0))
print(sum_product([45, 23, 76, 99, 12, 344], 1))