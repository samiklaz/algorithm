"""
PROBLEM STATEMENT 
Designer PDF Viewer

When you select a contiguous block of text in a PDF viewer, the selection is highlighted
with a blue rectangle. In the PDF viewer, each word is highlighted differently.

In this challenge, you will be given a list of letters height in the alphabet and a
string. Using the letter heights given, determine the area of the rectangle Highlight in
mm^2 assuming all letters are 1mm wide.

For example, the highlighted word = torn. Assume the heights of the letters are t=2, o=1,
r=1 and n=1. The tallest letter is 2 high and there are 4 letters. The highlighted area
will be 2 * 4= 8mm^2 so the answer is 8.

CONDITIONS

SAMPLE INPUT 
1   3   1
3

SAMPLE OUTPUT 
9

CONSTRAINT
"""


"""
My solution
def designerPdfViewer(h, word):
    n = len(word)
    return n * h

"""
def designerPdfViewer(h, word):
    height = 0
    for letter in word:
        height = max(height, h[ord(letter) - ord('a')])

    return height * len(word)


word = "abcz"
h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]

print(designerPdfViewer(h, word))