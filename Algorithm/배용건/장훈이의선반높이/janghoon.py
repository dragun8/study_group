import sys
sys.stdin = open('input.txt','r')


def dfs(idx, h_sum):
    global answer
    if h_sum >= B:
        answer = min(h_sum, answer - B)
        return
    
    if answer == 0:
        return
    
    if idx == N:
        return
    dfs(idx+1,h_sum + heights[idx])
    dfs(idx+1,h_sum)



T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))


    heights.sort(reverse=True)
    answer = float('inf') # 초과 높이중 최소높이

    
        
    dfs(0, 0) # 점원 0번부터, 누적합 0으로 DFS 시작
    
    if answer == float('inf'):
        answer = 0
    
    print(f"#{tc} {answer}")




