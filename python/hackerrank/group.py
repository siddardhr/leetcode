#Solution1
print("Hello, World!")

#Solution2
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

if n % 2 != 0:
    print("Weird")
else:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")

#Solution3
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print(a + b)
print(a - b)
print(a * b)

#Solution4
if __name__ == '__main__':
    n = int(input())

for i in range(n):
    print(i**2)

#Solution5
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print(a//b)
print(a/b)

#Solution6
T = int(input())

for _ in range(T):
    N = input()
    try:
        float(N)
        if '.' in N:
            print(True)
        else:
            print('False')
    except ValueError:
        print(False)

#Solution7
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(arr))
    arr.sort()
    print(arr[-2])
