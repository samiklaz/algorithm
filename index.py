"""
PROBLEM STATEMENT 

CONDITIONS

SAMPLE INPUT 
Bigger is Greater

Lexographical order is often known as alphabetical order when dealing with strings.
A string is greater than another string if it comes later in a lexographically sorted
list.

Given a word, create a new word by swapping some or all of its characters. These two
words must meet two criterias:
    - It must be greater than the original word.
    - It must be the smallest word that meets the first condition.

For example, given the word w=abcd, the next largest word is abdc

SAMPLE OUTPUT 

CONSTRAINT
"""

def biggerIsGreater(w):
    result = ""
    n = len(w)
    w = list(w)

    i = n-2 
    while i >= 0 and w[i] >= w[i+1]:
        i -= 1

    if i == -1:
        result = "no answer"
    else:
        j = n - 1
        while j >= i and w[j] <= w[i]:
            i -= 1

        w[i], w[j] = w[j], w[i]
        w = "".join(w)

        result = w[:i+1] + w[i+1:][::-1]
    return result
    


w = "bacdfe"
print(biggerIsGreater(w))


