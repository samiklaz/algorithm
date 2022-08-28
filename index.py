from collections import Counter

def beautifultriplets(d, arr):
    n = Counter(arr)

    print("counter n == ", n)
    count = 0

    for i, v in n.items():
        print("i == ", i, v)

    for num in arr:
        if n[num + d] and n[num + d + d]:
            
            count += 1
    return count



arr = [1, 2, 4, 5, 7, 8, 10]
d = 3
n = 7
print(beautifultriplets(d, arr))