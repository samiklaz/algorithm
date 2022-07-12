"""
PROBLEM STATEMENT 
You are incharge of the cake for your niece's birthday and have decided
the cake would have one candle for each year of her total age. When she
blows out the candles, she'll only be able to blow out the tallest ones. 
Find out how many candles she can successfully blow out. 

SAMPLE INPUT 
4 years old
arr = [4, 4, 1, 3]

SAMPLE OUTPUT 
2

"""

# solution 1 
def birthdayCakeCandles1(arr):
    n = len(arr)
    maximum = 0 
    count = 0 

    for i in range(n):
        if arr[i] > maximum:
            maximum = arr[i]
            count = 1
        elif arr[i] == maximum:
            count += 1

    return count


# Solution 2
def birthdayCakeCandles(arr):
    return arr.count(max(arr))


arr = [4, 4, 1, 3]
print(birthdayCakeCandles(arr))