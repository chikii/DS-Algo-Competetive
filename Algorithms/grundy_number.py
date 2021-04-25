def MEX(s):

    mex = 0
    # we set mex at lowest
    # then increase mex by one and if it is in set or not 
    # in this way we will get the smallest non negative number not present in set.
    while mex in s:
        mex += 1

    return mex

# this function will differ according to the game
# basic concept is this if grandy is 0 -> player with turn will loose the Game.
# else Win the Game.
def Grundy(n):
    """
    n = 0 loose game
    grundy(1) = mex(grundy(0)) -> 1 
    grundy(2) = mex(grundy(1), grundy(0))
              = mex(0, 1) -> 2
    grundy(3) = mex(grundy(2), grundy(1), grundy(0))
              = mex(2, 0, 1) -> 3
    """

    # base case 
    if n == 0:
        return 0
    if 1 <= n and n <= 3:
        return n
     
    return MEX({Grundy(n-1), Grundy(n-2), Grundy(n-3)})


# game is, - a pile has n coins. player can take upto 3 coins (1-3). player taking the last coin will win the game.
# This game is 1 pile version of Nim.

n = 8
print("If both player plays optimally then First player will ")
if Grundy(n) == 0:
    print('Loose Game')
else:
    print("Definetly Win Game.")