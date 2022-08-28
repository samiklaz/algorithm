"""
PROBLEM STATEMENT 
Halloween Game Sales

You wish to bu video games from the famous online video game store Mist.
Usually, all games are sold at the same price, p dollars. However, they 
are planning to have the seasonal Halloween Sale next month which you 
can buy games at a cheaper price. Specifically, the first game you buy 
during the sale will be sold at p dollars, but every subsequent game
you will buy will be sold at exactly d dollars less than the cost of the 
previous one you bought. 

This will continue until the cost becomes less than or equal to m dollars,
after which each game you will buy will cost m dollars each.

CONDITIONS

SAMPLE INPUT 

SAMPLE OUTPUT 

CONSTRAINT
"""

def howManyGames(p, d, n, s):
    games = 0     

    while p <= s:
        s -= p
        p = max(p-d, n)
        games += 1

    return games


p, d, n, s = 20, 3, 6, 100
print(howManyGames(p, d, n, s))