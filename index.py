"""
PROBLEM STATEMENT 
Drawing Book Master

Brie's drawing teacher asks her class to open their books to a page number.
Brie can either start turning pages from the front of the book or from the
back of the book. She always turn pages one at a time.

When she opens the book, page 1 is always on the right side:
When she flips from page 1, she sees page 2 and 3. Each page except the last
page will always be printed on both sides. The last page may only be printed
on the front, given the length of the book. If the book is n pages long, and 
she wants to turn to page p, what is the minimum number of pages she will
turn? She can start at the beginning or the end of the book.

Given n and p, find and print the minimum number of pages Brie must turn in
order to arrive at page p.

SAMPLE INPUT 
6
2

SAMPLE OUTPUT
1 

CONSTRAINT
1 <= n <= 10^5
1 <= p <= n
"""

def pageCount(n, p):
    front = p // 2

    if n%2 == 1:
        back = (n-p) // 2
    else:
        back = (n-p+1) // 2

    print(f'front - {front} and back - {back}')

    return min(front, back)

n = 6
p = 3

print(pageCount(n, p))

