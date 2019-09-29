#!/usr/bin/python3

# 旋转数组
def rotate(nums: list, k: int) -> None:
    for i in range(k):
        nums.insert(0, nums.pop(len(nums) - 1))


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(arr)
    rotate(arr, 3)
    print(arr)
