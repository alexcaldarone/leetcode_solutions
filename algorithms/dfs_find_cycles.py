# implementation of algorithm to find cycles in a directed graph using DFS

from typing import List, Dict
import pytest

def find_cycle(n: int, edges: List[List[int]]):
    adj_list = [[] for _ in range(n)]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    visited = set()
    def dfs(curr, par):
        if curr in visited:
            return False
        
        visited.add(curr)
        for nei in adj_list[curr]:
            if nei == par:
                continue

            # if false then neighbor has a cycle
            if not dfs(nei, curr):
                return False
        
        return True
    
    return dfs(0, -1) and len(visited) == n


# tests
def test_single_node_no_edges():
    # Connected & acyclic (tree)
    n = 1
    edges = []
    assert find_cycle(n, edges) is True

def test_line_tree():
    # 0-1-2-3 (tree)
    n = 4
    edges = [[0,1],[1,2],[2,3]]
    assert find_cycle(n, edges) is True

def test_star_tree():
    # 0 connected to all others (tree)
    n = 5
    edges = [[0,1],[0,2],[0,3],[0,4]]
    assert find_cycle(n, edges) is True

def test_simple_cycle_triangle():
    # 0-1-2-0 (cycle)
    n = 3
    edges = [[0,1],[1,2],[2,0]]
    assert find_cycle(n, edges) is False

def test_cycle_with_tail():
    # 0-1-2-0 is a cycle; 2-3 is a tail off the cycle
    n = 4
    edges = [[0,1],[1,2],[2,0],[2,3]]
    assert find_cycle(n, edges) is False

def test_disconnected_no_cycles():
    # Two components: (0-1) and (2-3). No cycles, but disconnected => False
    n = 4
    edges = [[0,1],[2,3]]
    assert find_cycle(n, edges) is False

def test_disconnected_with_cycle():
    # Component1: 0-1-2-0 (cycle), Component2: 3-4 (edge)
    n = 5
    edges = [[0,1],[1,2],[2,0],[3,4]]
    assert find_cycle(n, edges) is False

def test_self_loop_is_cycle():
    # Self-loop at node 0 creates a cycle
    n = 2
    edges = [[0,0], [0,1]]
    assert find_cycle(n, edges) is False

def test_two_edges_sharing_only_one_node_no_cycle():
    # 0-1 and 0-2 (tree)
    n = 3
    edges = [[0,1],[0,2]]
    assert find_cycle(n, edges) is True

def test_tree_larger():
    # A larger acyclic connected graph (tree)
    n = 7
    edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
    assert find_cycle(n, edges) is True

def _run_tests():
    def ok(n, edges, expected, name):
        got = find_cycle(n, edges)
        assert got is expected, f"{name} failed: expected {expected}, got {got}"

    ok(1, [], True, "single_node_no_edges")
    ok(4, [[0,1],[1,2],[2,3]], True, "line_tree")
    ok(5, [[0,1],[0,2],[0,3],[0,4]], True, "star_tree")
    ok(3, [[0,1],[1,2],[2,0]], False, "simple_cycle_triangle")
    ok(4, [[0,1],[1,2],[2,0],[2,3]], False, "cycle_with_tail")
    ok(4, [[0,1],[2,3]], False, "disconnected_no_cycles")
    ok(5, [[0,1],[1,2],[2,0],[3,4]], False, "disconnected_with_cycle")
    ok(2, [[0,0],[0,1]], False, "self_loop_is_cycle")
    ok(3, [[0,1],[0,2]], True, "two_edges_star")
    ok(7, [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], True, "tree_larger")
    print("✅ all tests passed")

if __name__ == "__main__":
    _run_tests()