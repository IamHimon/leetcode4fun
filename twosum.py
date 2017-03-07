class Solution(object):
    def twoSum( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j) and (nums[i] + nums[j] == target) and ([j, i] not in result):
                    result.append([i, j])
        if len(result):
            return result[0]


if __name__ == '__main__':
    print('main')
    nums = [3, 3]
    target = 6
    r = Solution.twoSum(nums, target)
    print(r)
