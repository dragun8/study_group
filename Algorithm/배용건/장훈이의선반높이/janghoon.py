T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    answer = [float('inf')] # 초과 높이중 최소높이

    def dfs(idx, total):
        

        if total >= B:
            answer = min(answer, total - B)
            return

        if idx == N:
            return
        
        dfs(idx + 1, total + heights[idx])
        # idx 번째 점원을 사용

        dfs(idx + 1, total)
        # idx 번째 점원을 사용하지 않는다
    dfs(0, 0) # 점원 0번부터, 누적합 0으로 DFS 시작
    print(f"#{tc} {answer}")




