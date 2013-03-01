import re
import sys

n = int(sys.stdin.readline())
arr = sys.stdin.readline().split(" ")

soma = 0
for i in arr:
	soma = soma + int(i)

print ((n+1)*n/2) - soma