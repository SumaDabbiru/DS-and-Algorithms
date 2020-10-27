# def groupAnagrams(words):
#     """
#     O(w*n*log(n) + n*w* log(w)) time
#     O(wn) space
#     n=length of longest word
#     w= number of words
#     :param words:
#     :return:
#     """
#     if len(words) == 0:
#         return []
#
#     sortedWords = ["".join(sorted(w)) for w in words]
#     indices = [i for i in range(len(words))]
#     indices.sort(key=lambda x: sortedWords[x])
#
#     result= []
#     currentAnagramGroup = []
#     currentAnagram = sortedWords[indices[0]]
#
#     for index in indices:
#         word = words[index]
#         sortedWord = sortedWords[index]
#
#         if sortedWord == currentAnagram:
#             currentAnagramGroup.append(word)
#             continue
#
#         result.append(currentAnagramGroup)
#         currentAnagramGroup = [word]
#         currentAnagram = sortedWord
#
#     result.append(currentAnagramGroup)
#
#     return result

def groupAnagrams(words):
    """
    using Hashmaps
    O(w*n*log(n)) time
    O(wn) space
    n=length of longest word
    w= number of words
    :param words:
    :return:
    """
    anagrams = {}

    for word in words:
        print(word, sorted(word))
        sortedWord = "". join(sorted(word))
        print(sortedWord)
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]

    print(anagrams)

    return list(anagrams.values())

words=["yo", "wow", "cinema", "iceman", "oy", "oww", "wwo"]
print(groupAnagrams(words))