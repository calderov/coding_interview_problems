
import time

# Runtime 0.14 segundos
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
