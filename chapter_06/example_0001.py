#!/usr/bin/python3

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        elif n == 2:
            return 2
        step = [1, 1]
        for i in range(2, n + 1):
            step.append(step[i - 2] + step[i - 1])
        return step.pop()




if __name__ == '__main__':
    # 简单的问候一下世界
    print(Solution().climbStairs(4))