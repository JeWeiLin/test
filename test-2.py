# def findMaxMedianSum(nums):
#     n = len(nums)
#     if n < 3:
#         return 0
    
#     # 1. 排序
#     nums.sort()
    
#     total_median_sum = 0
#     num_groups = n // 3
    
#     # 2. 從右向左取中位數
#     # 每一組會消耗掉最右邊的兩個數（最大和次大）
#     # 次大值位於 index: (n - 2), (n - 4), (n - 6)...
#     # 我們總共取 num_groups 次
    
#     current_index = n - 2
#     for _ in range(num_groups):
#         total_median_sum += nums[current_index]
#         current_index -= 2
        
#     return total_median_sum


def detectFirstAnomaly(metrics):
    if len(metrics) < 2:
        return -1
    
    max_elements = metrics[0]
    
    for i, val in enumerate(metrics[1:], start=1):
        if val >= 3 * max_elements:
            return i
        if val > max_elements:
            max_elements = val
            
    return -1

metrics = [3, 10, 2, 7]

print(detectFirstAnomaly(metrics))



def findMaxMedianSum(nums):
    nums.sort()
    n = len(nums)
    k = n // 3  # 我們需要組成的組數
    
    # 從倒數第 2 個 (n-2) 開始往回數，每隔 2 個取一個，總共取 k 個
    # [開始索引 : 結束索引 : 步長]
    return sum(nums[n-2 : n-2*k-1 : -2])

nums = [2, 3, 4, 3, 4, 22]
print(findMaxMedianSum(nums))



# def multiply(numbers):
#     total = 1

#     for i in numbers:
#         total *= i 
    
#     return(total)

# print(multiply((8, 2, 3, -1, 7))) 

# def reverse(str1):
#     chars = []

#     for i in range(len(str1) - 1, -1, -1):
#         chars.append(str1[i])

#     return "".join(chars)

# print(reverse("IBM Data Engineer"))

# b = lambda x, y : x**3 + y 

# print(b(2, 5))