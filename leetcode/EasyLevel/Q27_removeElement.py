def removeElement(nums: List[int], val: int) -> int:
    k = 0  # Pointer for placing non-val elements

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]  # Place the non-val element at index k
            k += 1  # Move pointer forward

    return k