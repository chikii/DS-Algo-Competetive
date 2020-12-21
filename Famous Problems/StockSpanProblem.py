"""
price of stock is given for n days
canlculate the span for each day. 
span means no. of days before the current day stock has lesser or same price + today.

ex ->       n_Days = [100,80,60,70,60,75,85]
span_for_each_daya = [1,  1, 1, 2, 1, 4, 6]
"""
# We Solve problem using stack....observe the problem it is sliding window

stack = []
"""
-<___________
-           -
- -<_______ -
- - <__   - -
- -   -   - -
- - - - - - -
- - - - - - -
"""
price = [100,80,60,70,60,75,85]
n = len(price)
ans = []
for i in range(n):

    while len(stack) != 0 and price[stack[-1]] <= price[i]:
        stack.pop()
    
    if len(stack) == 0 : ans.append(i+1)
    else: ans.append(i - stack[-1])

    stack.append(i)

print(ans)



























