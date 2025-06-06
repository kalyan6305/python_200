# Biryani classes
# According to a recent survey, Biryani is the most ordered food. Chef wants to learn how to make world-class Biryani from a MasterChef. Chef will be required to attend the MasterChef's classes for X weeks, and the cost of classes per week is Y coins. What is the total amount of money that Chef will have to pay?

# Input Format
# The first line of input will contain an integer T.
# T — the number of test cases. The description of  T.

# T test cases follows.
# The first and only line of each test case contains two space-separated integers X and Y, as described in the problem statement.

# Output Format
# For each test case, output on a new line the total amount of money that Chef will have to pay.

# Constraints
#1≤T≤10
# 1≤X,Y≤100
#simple:1-input .
4
1 10
1 15
2 10
2 15

output
10
15
20
30


SLOUTION = """# Path: DAY-1.PY



for _ in range (int(input())):
    x,y=list(map(int,input().split()))
    print(x*y)
