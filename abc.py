from queue import PriorityQueue 

def best_first_search(graph,start,goal):
    frontier = PriorityQueue()
    frontier.put((0,start))
    explored = set()
    while not frontier.empty():
        current_cost, current_node = frontier.get()
        if current_node == goal:
            return true
        explored.add(current_node)
        if neighbour not in explored:
            Priority = cost
            frontier.put((Priority,neighbour))
    return false 
graph = [
    [(1,4),(2,2)],
    [(3,5)],
    [(3,8),4,10],
    [(5,3)],
    [(5,2)],
[]]
print(graph)
start_node = 0
goal_node = 5
print("path: ")
print(start_node)
best_first_search(graph, start_node, goal_node)
print(goal_node)   