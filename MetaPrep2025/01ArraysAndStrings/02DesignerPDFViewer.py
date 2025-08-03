# Designer PDF Viewer
# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

def designerPdfViewer(h, word):
    maxH = 0

    for c in word:
        index = ord(c) - ord('a')
        maxH = max(h[index], maxH)

    return len(word) * maxH

if __name__=="__main__":
    # Example 1
    h = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
    word = "abc"
    expected = 9
    output = designerPdfViewer(h, word)

    print(h)
    print(word)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2
    h = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7]
    word = "zaba"
    expected = 28
    output = designerPdfViewer(h, word)

    print(h)
    print(word)
    print(expected)
    print(output)
    print(expected == output)
    print()