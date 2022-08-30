"""
PROBLEM STATEMENT 
Lisa Workbook

Lisa just got a new math workbook. A workbook contains exercise problems, 
grouped into chapters. Lisa believes a problem to be special if its index
(within a chapter) is the same as the page number where it is located. The
formtat of Lisa's book is as follows:
    - There are n chapters in Lisa's workbook, numbered from 1 to n.
    - The ith chapter has arr[i] problems, numbered from 1 to arr[i].
    - Each Page can hold up to k problems. Only a chapter's last page
      of exercises may contain fewer than k problems. 
    - Each new Chapter starts on a new page, so a page will never contain
      problems from more than one chapter.
    - The page number indexing starts at 1.
Given the details for Lisa's workbook, can you count the number of its
special problems?

CONDITIONS

SAMPLE INPUT 

SAMPLE OUTPUT 

CONSTRAINT
"""

def workbook(n, k, arr):
    answer = 0
    page = 1

    for probs in arr:
        print("probs, range == ", probs, range(1, probs+1))
        for index in range(1, probs+1):
            if index == page:
                answer += 1

            if index == probs or index % k == 0:
                page += 1
    return answer


n = 5
k = 3
arr = [4, 2, 6, 1, 10]
print(workbook(n, k, arr))