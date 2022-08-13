"""
PROBLEM STATEMENT
You have a string of lowercase English alphabetical letters. You can  
perform two types of operations on the string.
1.  Append a lowercase English alphabetical letter to the end of the
    string.
2.  Delete the last character in the string. Performing this operation
    in an empty string results in an empty string.

Given an integer, k, and two digits of  string, s and k, determine 
whether or not you can convert s to t by performing exactly k of the 
above operation on s. If it's possible, print YES. Otherwise print NO.

CONDITIONS

SAMPLE INPUT 
hackerhappy
hackerank
5

SAMPLE OUTPUT 

CONSTRAINT
"""

def appendAndDelete(s, t, k):
    count = 0
    for i, j in zip(s, t):
        if i == j:
            count += 1
        else:
            break

    t_len = len(s) + len(t)

    # Case 1
    # t_len <= 2 * count + k

    # Case 2 
    # t_len % 2 == k % 2: YES

    # Case 3
    # t_len < k 
    # case 1 and case 2 or case 3

    if t_len <= 2 *count + k and t_len % 2 == k % 2 or t_len < k:
        return 'yes'
    else:
        return 'no'

s = "hackerhappy"
t = "hackerank"
k = 5
print(appendAndDelete(s, t, k))