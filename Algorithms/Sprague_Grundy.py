#This theorem is for partial games
# it says Player A and B both plays optimally then at current state of game
# if 'XOR' of Grundy all possible next subGame is non-zero then player having turn will win the game.
# else if it is 0 then player will loose game, now matter what (destined to loose)
#

# Let's take it example game of nim
# we have 3 piles having different coin in each pile, player can take upto 3 (1 to 3) coin at once,.
# player taking coin at last will win the game.
# this is the game of nim.  


def MEX(s):
    mex = 0
    while mex in s:
        mex += 1

    return mex

def  Grundy(n):
    if n == 0:
        return 0
    if 1 <= n and n <= 3:
        return n
    
    return MEX({Grundy(n-1), Grundy(n-2), Grundy(n-3)})

def solve(n):
    #Xor(grundy of all possible subgames)
    ans = 0
    for i in n:
        ans ^= Grundy(i)

    return ans

solve([0,4,1])