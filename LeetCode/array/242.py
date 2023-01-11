# https://leetcode.com/problems/valid-anagram/

def is_anagram(s: str, t: str) -> bool:
    counter1 = build_counter(s)
    counter2 = build_counter(t)

    return counter1 == counter2


def build_counter(word: str) -> dict:
    counter = dict()
    for char in word:
        if char not in counter:
            counter[char] = 1
            continue
        counter[char] += 1
    return counter

print(is_anagram('anagram', 'nagaram'))