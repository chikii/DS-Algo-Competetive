class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(5)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right.right = TreeNode(6)

from collections import deque


def merge(left, right, curr_seq, ans):
    """
    # intution -> 
        curr_seq = 0
        left  ->  1 2 3
        right ->  4 5 6

        use two pointer i, j on left and right
        now we can select either i or j to extend curr_seq

        curr_seq = 0 1
        left  ->  2 3
        right ->  4 5 6

        or 

        curr_seq = 0 4
        left  ->  1 2 3
        right ->  5 6

        in this way we can solve recurssively to get curr_seq
        and at any point if left or right seq become empty just copy all the seq form remaining list to curr_seq,
        and add in ans.
    """


    if not left or not right:
        curr_ans = deque(curr_seq)
        curr_ans.extend(left)
        curr_ans.extend(right)
        ans.append(curr_ans)
        return
    
    top = left.popleft()
    curr_seq.append(top)
    merge(left, right, curr_seq, ans)
    curr_seq.pop()
    left.appendleft(top)

    top = right.popleft()
    curr_seq.append(top)
    merge(left, right, curr_seq, ans)
    curr_seq.pop()
    right.appendleft(top)



def solve(root):
    if root == None : return [deque([])]
    if root.left == None and root.right == None: return [deque([root.val])]


    left_ans = solve(root.left)
    right_ans = solve(root.right)


    ret = []    
    prefix = deque([root.val])

    # now we have some ans for left and some ans for right, and every one can make combination with other, that's why nested loop
    for left in left_ans:
        for right in right_ans:
            # we will find all the possible way of merge left and right with current root.
            merge(left, right, prefix, ret) # in how many ways we can put len(left) in (len(left)+len(right)) places -> nCr - n! / r!*(n-r)!

    return ret

ans = solve(root)
c = 0
for i in ans:
    print(c, '-', list(i))
    c += 1
