import heapq

class Pathfinder:
    def __init__(self, start_coords, dest, map):
        self.start_coords = start_coords
        self.dest = dest
        self.map = map

    def calc_h(self, node, dest):
        # Manhattan distance
        return abs(dest[0] - node[0]) + abs(dest[1] - node[1])

    def get_neighbors(self, node):
        neighbors = []
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = node[0] + dx, node[1] + dy
            # Check bounds before accessing map
            if 0 <= nx < self.map.width and 0 <= ny < self.map.height:
                if self.map.get_num(nx, ny) == 0:  # Open
                    neighbors.append((nx, ny))
        return neighbors

    def reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

    def find_path(self):
        start = tuple(self.start_coords)
        goal = tuple(self.dest)
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.calc_h(start, goal)}
        closed_set = set()

        while open_set:
            _, current = heapq.heappop(open_set)
            if current == goal:
                return self.reconstruct_path(came_from, current)

            closed_set.add(current)
            for neighbor in self.get_neighbors(current):
                if neighbor in closed_set:
                    continue
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.calc_h(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
        return []  # No path found