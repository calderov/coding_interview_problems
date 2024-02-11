
# Given a list of 1 million numbers and a list of half a million numbers,
# remove all the items in the second list from the first one in less than
# one second.

import time

# Runtime 0.14 seconds
def RemoveElementsFromList(original, elements):
    return sorted(set(original).difference(set(elements)))

if __name__ == "__main__":
    original = list(range(1, int(1e6) + 1))
    elements = list(range(2, int(1e6) + 1, 2))

    start = time.time()
    original = RemoveElementsFromList(original, elements)
    print(original[:10])
    end = time.time()

    print(end - start)
