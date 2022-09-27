def array_front9(nums):
    nine = 0
    for numbers in range(nums[0:5]):
        if numbers == 9:
            nine = nine + 1        
    if nine > 0:
        return True
    else:
        return False
