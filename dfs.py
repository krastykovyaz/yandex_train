# 31. Поиск в глубину

# Дан неориентированный граф, возможно, с петлями и кратными ребрами. Необходимо построить компоненту связности, содержащую первую вершину.

# Формат ввода
# В первой строке записаны два целых числа N (1 ≤ N ≤ 103) и M (0 ≤ M ≤ 5 * 105) — количество вершин и ребер в графе. В последующих M строках перечислены ребра — пары чисел, определяющие номера вершин, которые соединяют ребра.

# Формат вывода
# В первую строку выходного файла выведите число K — количество вершин в компоненте связности. Во вторую строку выведите K целых чисел — вершины компоненты связности, перечисленные в порядке возрастания номеров.


if __name__=='__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for i, j in [tuple(map(int, input().split())) for _ in range(m)]:
        graph[i].append(j)
        graph[j].append(i)

    color = [False for _ in range(n + 1)]


    def dfs(ver):
        color[ver] = True
        for u in graph[ver]:
            if not color[u]:
                dfs(u)


    dfs(1)

    vertex = []
    for v in range(1, n + 1):
        if color[v]:
            vertex.append(v)

    print(vertex[-1])
    print(*vertex)