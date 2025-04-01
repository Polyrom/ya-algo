def find_min_element_idx(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return left


def broken_search(nums, target):
    min_element_idx = find_min_element_idx(nums)
    if target == nums[min_element_idx]:
        return min_element_idx

    left, right = 0, 0
    if min_element_idx == 0:
        left, right = 0, len(nums) - 1
    elif target >= nums[0]:
        left, right = 0, min_element_idx - 1
    elif target < nums[0]:
        left, right = min_element_idx + 1, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
    arr = [12, 41, 122, 411, 412, 1222, 3000, 12222, 122222]
    assert broken_search(arr, 3000) == 6


if __name__ == "__main__":
    test()
