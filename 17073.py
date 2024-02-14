# https://www.acmicpc.net/problem/17073

# 나무 위의 빗물

# 문제

 

# 트리란, 사이클이 없는 연결 그래프를 의미한다. 위 그림은 1번 정점을 루트로 하는 어떤 트리를 나타낸 모습이다.

# 사실 이 트리는 영훈이가 뒷마당에서 기르고 있는 나무이다. 어제는 비가 왔기 때문에, 트리의 1번 정점에는 W만큼의 물이 고여 있다. 1번 정점을 제외한 모든 정점에는 아직 물이 고여 있지 않은 상태이다.

# 이제 매초마다 모든 정점은 아래의 작업을 순서대로 반복한다.

# 물을 가지고 있으며, 자식 정점이 있다면 자식 정점 중 하나를 골라 물을 1 준다. 자식 정점이 여러 개라면 동일한 확률로 그 중 하나를 고른다.
# 만약 부모 정점이 자신에게 물을 흘려보냈다면 받아서 쌓아 둔다.
# 이때, 위 작업은 순서대로 진행되므로 부모 정점에게 받은 물을 즉시 자식 정점에게 줄 수는 없다.

# 영훈이는 나무를 바라보면서 더 이상 물이 움직이지 않는 상태가 되었을 때 각 정점에 어느 정도의 물이 있게 될지 궁금해졌다. 더 이상 물이 움직이지 않을 때, i번 정점에 쌓인 물의 양의 기댓값을 Pi라 하자. 이때, Pi가 0보다 큰 정점들에 대해서 Pi들의 평균은 어느 정도가 될까?

# 입력
# 첫째 줄에 트리의 노드의 수 N과 1번 노드에 고인 물의 양을 의미하는 정수 W가 주어진다. (2 ≤ N ≤ 500,000, 1 ≤ W ≤ 109)

# 다음 N-1줄에 걸쳐, 트리에 존재하는 간선의 정보가 U V의 형태로 주어진다. (1 ≤ U, V ≤ N​​​​, U ≠ V)

# 이는 양 끝 정점이 각각 U와 V인 간선이 트리에 존재한다는 의미이다.

# 입력으로 주어지는 트리는 항상 올바른 연결 트리임이 보장되며, 주어지는 트리의 루트는 항상 1번 정점이다.

# 출력
# 문제의 정답을 출력한다. 정답과의 차이가 10-3 이하인 값은 모두 정답으로 인정된다.

from collections import defaultdict

def calculate_expected_water_distribution(n, w, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    water_distribution = defaultdict(int)
    water_distribution[1] = w
    visited = set()

    def dfs(node):
        visited.add(node)
        num_children = len([child for child in graph[node] if child not in visited])
        if num_children == 0:
            return
        water_per_child = water_distribution[node] / num_children
        for child in graph[node]:
            if child not in visited:
                water_distribution[child] += water_per_child
                dfs(child)

    dfs(1)

    leaf_nodes_water = [water_distribution[node] for node in water_distribution if len(graph[node]) == 1 and node != 1]
    average_water = sum(leaf_nodes_water) / len(leaf_nodes_water)
    return average_water

if __name__ == "__main__":
    n, w = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
    average_water_at_leaf_nodes = calculate_expected_water_distribution(n, w, edges)
    print(f"{average_water_at_leaf_nodes:.10f}")