__author__ = 'TTc9082'
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        nd = {}
        for i in range(len(num)):
            nd[num[i]] = [i+1] if num[i] not in nd else nd[num[i]] + [i+1]
        for n in num:
            if target - n in nd:
                if len(nd[n]) > 1:
                    return (nd[n][0], nd[n][1])
                elif nd[n] != nd[target - n]:
                    return (nd[n][0], nd[target - n][0])

    def twoSum2(self, num, target):
        cn = num[:]
        cn.sort()
        l = 0
        r = len(num) - 1
        index = []
        while l < r:
            sum = cn[l] + cn[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            elif sum == target:
                for i in range(len(num)):
                    if num[i] == cn[l]:
                        index.append(i+1)
                    elif num[i] == cn[r]:
                        index.append(i+1)
                    if len(index) == 2:
                        break
                break
        return (index[0], index[1])

print Solution().twoSum2([0,4,0], 0)