from heapq import heappop, heappush

# ダイクストラ法(始点sから各頂点への最短距離)、オーダー: MlogN, N:ノード数, M:エッジ数
# d: 各頂点へのコスト(存在しないときはinf)
# q: キュー(スタートからのコスト, 頂点)
# 参考: https://atcoder.jp/contests/abc035/tasks/abc035_d
def dijkstra(start: int, node_num: int, edge: list) -> list:
    d = [float("inf")] * node_num
    d[start] = 0
    #スタートをキューに入れる
    q = [(0,start)]

    while len(q) != 0:
        #キューの先頭を取得
        ci, i = heappop(q)
        if d[i] < ci:
            continue
        #キューの先頭から繋がっている頂点を探索
        for cj, j in edge[i]:
            if d[j] > d[i] + cj:
                d[j] = d[i] + cj
                heappush(q, (d[j], j))
                
    return d