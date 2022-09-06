# def convert_base(number, base):
#     if base < 2:
#         return False
#     remainders = []
#     while number > 0:
#         remainders.append(str(number % base))
#         number //= base
#     remainders.reverse()
#     return int(''.join(remainders))

# class Solution:
# def findSubarrays(nums):
#     lists = [[]]
#     for i in range(len(nums) + 1):
#         for j in range(i):
#             lists.append(nums[j: i])
#     for i in lists:
#         if lists.count(i)>1:
#             return False
#     return True
# print(findSubarrays([4,2,4]))
def convert_base(number, base):
        if base < 2:
            return False
        remainders = []
        while number > 0:
            remainders.append(str(number % base))
            number //= base
        remainders.reverse()
        return int(''.join(remainders))
print(convert_base(111,5))