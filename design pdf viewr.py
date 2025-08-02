def designerPdfViewer(h, word):
    max_height = 0
    for char in word:
        index = ord(char) - ord('a')
        max_height = max(max_height, h[index])
    
    return max_height * len(word)

# Input
h = list(map(int, input().split()))
word = input()

# Output
print(designerPdfViewer(h, word))
