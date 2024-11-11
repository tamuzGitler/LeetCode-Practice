def findMissingRanges(nums):
    # nums is sorted
    # range of numbers [0,99]
    lower = 0
    upper = 99
    if len(nums) == 0:
        return ["0->99"]
    missingRanges = []
    if (nums[0] != 0):
        if nums[0] == 1:
            missingRanges.append("0")
        else:
            missingRanges.append("0->" + str(nums[0] - 1))
        lower = nums[0] + 1
    for i in range(1, len(nums)):

        if nums[i] - nums[i - 1] == 2:
            missingRanges.append(str(lower))
        elif nums[i] - nums[i - 1] > 2:
            s = str(lower) + "->" + str(nums[i] - 1)
            missingRanges.append(s)
        lower = nums[i] + 1

    if lower == 99:
        missingRanges.append("99")
    else:
        s = str(lower) + "->99"
        missingRanges.append(s)

    # deal with last range
    return missingRanges


if __name__ == '__main__':
    nums = [2, 5, 96]
    print(findMissingRanges(nums))
