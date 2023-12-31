
class Solution:
    def twoSum(self, nums, target: int):
        for num in nums:
            if target < 0:
                    remainder = target - num
                    if remainder in nums:
                        if remainder == num:
                            try:
                                return [nums.index(num), nums.index(remainder, nums.index(num)+1)]
                            except:
                                continue
                        return [nums.index(num), nums.index(remainder)]
                    else:
                        continue
            else:
                if num > target:
                    continue

                remainder = target - num
                if remainder in nums:
                    if remainder == num:
                        try:
                            return [nums.index(num), nums.index(remainder, nums.index(num)+1)]
                        except:
                            continue
                    return [nums.index(num), nums.index(remainder)]
                else:
                    continue




if __name__ == '__main__':
    nums = [-1,-2,-3,-4,-5]
    target = -8

    # Object for class Solution
    s = Solution()
    print(s.twoSum(nums, target))