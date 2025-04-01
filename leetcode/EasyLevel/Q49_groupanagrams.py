from collections import defaultdict

def groupAnagrams(strs: List[str]) -> List[List[str]]:

    anagram_dict = defaultdict(list)  # Dictionary to store anagram groups

    for word in strs:
        sorted_word = "".join(sorted(word))  # Sort the word alphabetically
        anagram_dict[sorted_word].append(word)  # Add to the respective group

    return list(anagram_dict.values())  # Convert dictionary values to a list