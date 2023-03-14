DEFAULT_COLOR = 0

if __name__=='__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)

    colors = [DEFAULT_COLOR for _ in range(n+1)]
    def dfs(vert, cnt, comp):
        colors[vert] = cnt
        comp.append(vert)
        for v in graph[vert]:
            if not colors[v]:
                dfs(v, cnt, comp)


    cnt = 0
    comps = []
    for v in range(n + 1):
        comp = []
        if not colors[v]:
            cnt += 1
            dfs(v, cnt, comp)
        comps.append(comp)

    # vertex = []
    # for i in range(n):
    #     vertex.append(colors[i])
    # print(components)
    comps = [c  for c in comps if any(c)]
    length = len(comps)
    print(length)
    for comp in comps:
        print(length)
        print(*comp)
        length -= 1



    print(graph, colors, comps)
