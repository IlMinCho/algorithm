# https://www.acmicpc.net/problem/14675

# 단절점과 단절선
# 문제
# 그래프 이론에서 단절점(cut vertex)과 단절선(bridge)은 다음과 같이 정의 된다.

# 단절점(cut vertex) : 해당 정점을 제거하였을 때, 그 정점이 포함된 그래프가 2개 이상으로 나뉘는 경우, 이 정점을 단절점이라 한다.
# 단절선(bridge) : 해당 간선을 제거하였을 때, 그 간선이 포함된 그래프가 2개 이상으로 나뉘는 경우, 이 간선을 단절선이라 한다.
# 이 단절점과 단절선을 우리는 트리(tree)에서 구하려고 한다. 그래프 이론에서 트리(tree)의 정의는 다음과 같다.

# 트리(tree) : 사이클이 존재하지 않으며, 모든 정점이 연결되어 있는 그래프
# 트리의 정보와 질의가 주어질 때, 질의에 대한 답을 하시오. 

# 입력
# 프로그램의 입력은 표준 입력으로 받는다. 입력의 첫 줄에는 트리의 정점 개수 N이 주어진다. (2 ≤ N ≤ 100,000) 트리의 정점은 1번부터 n번까지 존재한다. 다음 줄부터 N-1개의 줄에 걸쳐 간선의 정보 a, b가 주어진다. 이는 a정점과 b정점이 연결되어 있다는 뜻이며, 입력으로 주어지는 정보는 트리임이 보장된다. (1 ≤ a, b ≤ N)

# 다음 줄에는 질의의 개수 q가 주어진다. (1 ≤ q ≤ 100,000) 다음 q줄에는 질의 t k가 주어진다. (1 ≤ t ≤ 2) t가 1일 때는 k번 정점이 단절점인지에 대한 질의, t가 2일 때는 입력에서 주어지는 k번째 간선이 단절선인지에 대한 질의이다. t가 1일 때는 (1 ≤ k ≤ n)이며, t가 2일 때는 (1 ≤ k ≤ n - 1)이다. 

# 출력
# 프로그램의 출력은 표준 출력으로 한다. q줄에 대하여 해당 질의에 대한 답을 한다. 각각은 개행으로 구분하며, 질의가 맞다면 ‘yes’를, 질의가 틀리면 ‘no’를 출력한다. 


# n = int(input())  # 트리의 정점 개수
# edges = [tuple(map(int, input().split())) for _ in range(n - 1)]  # 간선 정보

# # 질의 개수
# q = int(input())
# queries = [tuple(map(int, input().split())) for _ in range(q)]  # 질의 정보

# # 트리에서 모든 간선은 단절선이다.
# # 단절점 여부를 판단하기 위해 각 정점의 자식 수를 계산한다.
# children_count = [0] * (n + 1)
# for a, b in edges:
#     children_count[a] += 1
#     children_count[b] += 1

# for t, k in queries:
#     if t == 1:  # 단절점 질의
#         # 루트가 아닌 정점이고 자식이 2개 이상이면 단절점이다.
#         # 트리에서는 루트 노드를 제외한 모든 내부 노드가 단절점이 될 수 있다.
#         # 여기서는 간단히 처리하기 위해 자식이 1개 이상인지만 확인한다.
#         print('yes' if children_count[k] > 1 else 'no')
#     elif t == 2:  # 단절선 질의
#         # 트리에서 모든 간선은 단절선이다.
#         print('yes')



# n = int(input())  # 트리의 정점 개수
# graph = [[] for _ in range(n + 1)]

# # 그래프 구성
# for _ in range(n - 1):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# order = 0  # 노드 방문 순서
# orders = [-1] * (n + 1)  # 각 노드의 방문 순서
# low = [-1] * (n + 1)  # 각 노드에서 도달할 수 있는 가장 낮은 순서
# is_cut_vertex = [False] * (n + 1)  # 단절점 여부

# def dfs(node, parent):
#     global order
#     order += 1
#     orders[node] = low[node] = order
#     child_count = 0  # 루트 노드의 자식 수

#     for next_node in graph[node]:
#         if next_node == parent:
#             continue
#         if orders[next_node] == -1:  # 아직 방문하지 않은 노드
#             child_count += 1
#             dfs(next_node, node)
#             low[node] = min(low[node], low[next_node])
#             # 루트가 아닌 노드에서 조건을 만족하면 단절점
#             if parent != 0 and low[next_node] >= orders[node]:
#                 is_cut_vertex[node] = True
#         else:
#             low[node] = min(low[node], orders[next_node])

#     # 루트 노드인 경우
#     if parent == 0 and child_count >= 2:
#         is_cut_vertex[node] = True

# dfs(1, 0)  # 1번 노드를 루트로 가정

# # 질의 처리
# q = int(input())
# for _ in range(q):
#     t, k = map(int, input().split())
#     if t == 1:  # 단절점 질의
#         print('yes' if is_cut_vertex[k] else 'no')
#     elif t == 2:  # 단절선 질의
#         print('yes')  # 트리에서 모든 간선은 단절

import sys
input=sys.stdin.readline

N=int(input())
Tree=[ [] for _ in range(N+1) ]

for i in range(N-1):
    a,b=map(int,input().split())
    Tree[a].append(b)
    Tree[b].append(a)

Q=int(input())

for i in range(Q):
    a,b=map(int,input().split())

    if a==2:
        print("yes")
    else:
        if len(Tree[b])>=2:
            print("yes")
        else:
            print("no")