import sys

# cut-edge-through
def DFS(L, weight, weight_sum, check_sum):
    if sum(nums) - check_sum + weight_sum < res[0]:
        return
    elif weight_sum > weight:
        return
    elif L == len(nums):
        if res[0] < weight_sum:
           res[0] = weight_sum
    else:
        DFS(L + 1, weight, weight_sum + nums[L], check_sum + nums[L])
        DFS(L + 1, weight, weight_sum, check_sum + nums[L])

if __name__ == '__main__':
    weight = 259
    nums = [81, 58, 42, 33, 61]
    temp = [0] * len(nums)
    weight_sum = 0
    check_sum = 0
    res = [0]
    DFS(0, weight, weight_sum, check_sum)

    print(res)