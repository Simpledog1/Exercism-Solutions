def find_anagrams(word, candidates):
    result = []
    word = word.lower()
    for candidate in candidates:
        if candidate.lower() != word:
            if sorted(word) == sorted(candidate.lower()):
                result.append(candidate)
    return result