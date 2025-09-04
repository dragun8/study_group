import sys
import itertools
sys.stdin = open(".txt","r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    carrot = list(map(int, input().split()))
    carrot.sort()
    s = []
    m = []
    l = []
    

