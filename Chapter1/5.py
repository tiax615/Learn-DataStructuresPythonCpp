import math

'''
nums: [11, 22, 33, 44, 55, 66, 77, 88, 99]
max score: 99.0
min scors: 11.0
average: 495.0
std deviation: 495.0
'''

def get_scores():
    ''' Get scores interactively from the user
    post: returns a list of numbers obtained from user '''
    pass

def min_value(nums):
    ''' find the minimum
    pre: nums is a list of numbers and len(nums) > 0
    post: returns smallest number in nums '''
    return min(nums)

def max_value(nums):
    '''find the maximum
    pre: nums is a list of numbers and len(nums) > 0
    post: returns largest number in nums '''
    return max(nums)

def average(nums):
    ''' calculate the mean
    pre: nums is a list of numbers and lens(nums) > 0
    post: returns the mean (a float) of the values in nums '''
    sum = 0
    for num in nums:
        sum += num
    return sum

def std_deviation(nums):
    ''' calculate the standard deviation
    pre: nums is a list of numbers and len(nums) > 1
    post: returns the standard deviation (a float) of the v in nums '''
    xbar = average(nums)
    sum = 0
    for num in nums:
        sum += (xbar - num) ** 2
    return math.sqrt(sum / (len(nums) - 1))

def print_res(nums):
    print('nums:', nums)
    print('max score: %.1f' % max_value(nums))
    print('min scors: %.1f' % min_value(nums))
    print('average: %.1f' % average(nums))
    print('std deviation: %.1f' % average(nums))

def main():
    nums = [11,22,33,44,55,66,77,88,99]
    print_res(nums)

if __name__ == '__main__':
    main()