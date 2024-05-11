def countingSort(nums, k):
    # O(n+k) / O(n) - good if we know k
    c = [0] * (k + 1)
    ans = [0] * len(nums)
    for num in nums:
        c[num] += 1
    for i in range(1, len(c)):
        c[i] += c[i - 1]
    for num in nums:
        ans[c[num] - 1] = num
        c[num] -= 1

    return ans


if __name__ == '__main__':
    nums = [1, 4, 1, 2, 7, 5, 2]
    print(countingSort(nums, 9))
  