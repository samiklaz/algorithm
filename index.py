"""
PROBLEM STATEMENT 
Anna and Brian are sharing a meal at a restaurant and they agree to split the bill.
Brian wants to order something that Anna is allergic to though, and they agree that
Anna won't pay for that item. Brian gets the cheque and calculates Anna's portion.
You must determine if the calculation is correct.

For example, assume the bill has the following prices, bill=[2, 4, 6]. Anna declines
to eat item k = bill[2] which costs 6. If Brian calculates the bill correctly, Anna
would pay (2+4) /2 = 3. If he includes the cost of bill[2], he will calculate 
(2 + 4 + 6) /2 = 6. In the second case, he refused to refund 3 to Anna.

SAMPLE INPUT 
The first line contains two space-seperated integer n and k, the number of items
ordered and the 0-based index of the item that Anna did not eat.

The second line contains n space-seperated integer bill[i], where 0 <= i <= n.

the third line contains an integer, b, the amount of money that Brian charged Anna
for her share of  the bill.

4 1
3 10 2 9 
12

SAMPLE OUTPUT 
5

CONSTRAINT
2 <= n <= 10^3
0 <= k < n
0 <= bill[i] <= 10^4
"""

def bomAppetit(bill, k, b):
    s = sum(bill)
    charges = (s - bill[k]) // 2

    if b == charges:
        print("Bom Appetit")
    else:
        print(b - charges)

bill = [3, 10, 2, 9]
k = 1
b = 12
bomAppetit(bill, k, b)
