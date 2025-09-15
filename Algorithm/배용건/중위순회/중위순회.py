class Node:  # Node 라는 class를 만들어줄거야
    def __init__(self,val):
        self.val = val  # 노드의 값
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드

def inorder(node, result):
    if node:
        inorder(node.left, result) # 왼쪽 서브트리 방문
        result.append(node.val)  # 현재 노드 방문
        inorder(node.right, result) # 오른쪽 서브트리 방문



for tc in range(1, 11):
    N = int(input())
    nodes = [None] + [Node('') for _ in range(N)]
    # nodes = [None, Node(''), Node(''), Node('') ... * N]

    for _ in range(N):
        line = input().split() # 입력값을 문자열로 받는다
        idx = int(line[0]) # 입력값의 변수 첫번째 인덱스 값은 정수로 할당한다
        val = line[1] # 입력값의 변수 두번째 인덱스 값은 문자열로 할당한다
        nodes[idx].val = val # nodes 배열에 각각 인덱스 값을 넣어준다

        if len(line) >= 3: # len 이 3이상이면 3번째 인덱스값은 왼쪽 자식 노드 
            left = int(line[2]) # 입력값의 3번째 인덱스를 정수로 받으면 그건 왼쪽이라는 변수에 할당한다 
            nodes[idx].left = nodes[left] # nodes 배열의 idx 값에 left 값을 할당해준다

        if len(line) >= 4: # len 이 4이상이면 4번째 인덱스값은 오른쪽 자식 노드
            right = int(line[3]) # 입력값의 4번째 인덱스를 정수로 할당한다 오른쪽 변수에
            nodes[idx].right = nodes[right] # nodes[idx].right 에 right값을 할당한다
    result = [] # result 빈 리스트를 만들고 
    inorder(nodes[1], result) # inorder 함수를 발동시킨다
    print(f"#{tc} {''.join(result)}")
    