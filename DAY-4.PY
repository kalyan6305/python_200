# Determine the Score
# Chef appeared for a placement test.

# There is a problem worth X points. Chef finds out that the problem has exactly 10 test cases. It is known that each test case is worth the same number of points.

# Chef passes N test cases among them. Determine the score Chef will get.

# NOTE: See sample explanation for more clarity.

# Input Format
# First line will contain 
# T
# T, number of test cases. Then the test cases follow.
# Each test case contains of a single line of input, two integers X and N, the total points for the problem and the number of test cases which pass for Chef's solution.
# Output Format
# For each test case, output the points scored by Chef.

# X is a multiple of 10

# Sample 1:
# Input

# 4
# 10 3
# 100 10
# 130 4
# 70 0
# Output
# 3
# 100
# 52
# 0
T = int(input())
for _ in range(T):
    X, N = map(int, input().split())
    print((X // 10) * N)








# //2ND CODE 
# 404 Not Found
# Chef's website has a specific response mechanism based on the HTTP status code received:

# If the response code is 404, the website will return NOT FOUND.For any other response code different from 404, the website will return FOUND.
# Given the response code as X, determine the website response.

# Input Format
# The first and only line of input contains a response code X.



# Output Format

# Output on a new line NOT FOUND, if the response code is 
# 404
# 404. Otherwise print FOUND.

# You may print each character of the string in uppercase or lowercase (for example, the strings FOUND, fouND, FouND, and found will all be treated as identical).
 
# Sample 1:
# Input
# Output
# 200
# FOUND

X = int(input())
if X == 404:
    print("NOT FOUND")
else:
    print("FOUND")