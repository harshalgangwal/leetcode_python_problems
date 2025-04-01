def lengthOfLastWord(s: str) -> int:
        words = s.split()  # Split string by spaces
        return len(words[-1]) if words else 0