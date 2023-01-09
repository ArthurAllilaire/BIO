from itertools import permutations
def num_words(word, n):
    """Returns the number of n letter words that can be created from word"""
    return set(permutations(word, n))

perms = num_words("abbc", 3)
counter = 0
for i in perms:
    counter += 1

print(perms)

print(counter)
