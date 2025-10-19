# implementation of djisktra algorithm
# find the shortest path from source node to all other nodes in a directed weighted graph with non-negative weights

import heapq
from typing import List, Dict, Tuple

def dijkstra(graph: Dict[str, List[Tuple[str, int]]], source: str):
    nodes = set(graph.keys())
    for _, nbrs in graph.items():
        for v, w in nbrs:
            if w < 0:
                raise ValueError("Must have non-negative weights")
            nodes.add(v)
    
    dist = {node: float("inf") for node in nodes}
    dist[source] = 0
    pq = [(0, source)] # store (distance, node) in priority queue

    while pq:
        curr_dist, u = heapq.heappop(pq)

        if curr_dist > dist[u]:
            continue

        for v, weight in graph.get(u, []):
            alt = curr_dist + weight
            if alt < dist[v]:
                dist[v] = alt
                heapq.heappush(pq, (alt, v)) # store new distance and node in priority queue
        
    return dist # return dictionary with distances

def test_dijkstra_directed():
    # 1) Your directed case where C is only reachable directly from A and D is unreachable from A
    graph1 = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1)],       # no path onward to C or D from B
        'C': [('A', 4)],       # no path onward to D from C
        'D': [('B', 5), ('C', 1)]  # D has outgoing edges but no incoming from A/B/C paths
    }
    expected1 = {'A': 0, 'B': 1, 'C': 4, 'D': float('inf')}
    assert dijkstra(graph1, 'A') == expected1

    # 2) Disconnected directed graph (no path to C)
    graph2 = {
        'A': [('B', 3)],
        'B': [],
        'C': []
    }
    result2 = dijkstra(graph2, 'A')
    assert result2['A'] == 0
    assert result2['B'] == 3
    assert result2['C'] == float('inf')

    # 3) Single-node graph
    graph3 = {'A': []}
    assert dijkstra(graph3, 'A') == {'A': 0}

    # 4) Directed graph with zero-weight edges
    graph4 = {
        'A': [('B', 0)],
        'B': [('C', 0)],
        'C': []
    }
    expected4 = {'A': 0, 'B': 0, 'C': 0}
    assert dijkstra(graph4, 'A') == expected4

    # 5) Reverse edge exists but is costly; check correct forward path
    graph5 = {
        'A': [('B', 2)],
        'B': [('C', 1)],
        'C': [('A', 10), ('D', 3)],
        'D': []
    }
    expected5 = {'A': 0, 'B': 2, 'C': 3, 'D': 6}
    assert dijkstra(graph5, 'A') == expected5

    # 6) Node only mentioned as neighbor (sink)
    graph6 = {'A': [('B', 5)]}
    result6 = dijkstra(graph6, 'A')
    assert result6['A'] == 0
    assert result6['B'] == 5

    print("✅ All directed Dijkstra tests passed successfully.")

if __name__ == "__main__":
    test_dijkstra_directed()