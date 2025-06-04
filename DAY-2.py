# Chef Plays Ludo
# Chef is playing Ludo. According to the rules of Ludo, a player can enter a new token into the play only when he rolls a 6 on the die.
# In the current turn, Chef rolled the number X on the die. Determine if Chef can enter a new token into the play in the current turn or not.
# Input Format
# The first line contains a single integer T — the number of test cases. Then the test cases follow.
# The first and only line of each test case contains one integer X — the number rolled by the Chef on the die.

# Output Format.
# For each test case, output on a new line "YES" if Chef can enter a new token into the play, and "NO" otherwise.
# Constraints

# input
3
1
6
3
# output
# NO
# YES
# NO


# SLOUTION = """# Path: DAY-2.PY
# Chef Plays Ludo


for _ in range(int(input())):
    x = int(input())
    if x == 6:
        print("YES")
    else:
        print("NO")
