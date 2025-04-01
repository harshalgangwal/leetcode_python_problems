def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""

    prefix = ""
    for chars in zip(*strs):  # Transpose the strings and iterate column-wise
        if len(set(chars)) == 1:  # Check if all characters in this column are the same
            prefix += chars[0]
        else:
            break  # Stop at the first mismatch

    return prefix