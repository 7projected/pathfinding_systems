class Pathfinder:
    def __init__(self, start_coords, dest, map):
        self.start_coords = start_coords
        self.dest = dest
        self.map = map

        self.current_coords = start_coords
        self.last_coords = None  # Track the last coordinate
        self.available_nodes = []

    def calc_h(self, node, dest):
        # Manhattan distance
        return abs(dest[0] - node[0]) + abs(dest[1] - node[1])

    def calc_g(self, node, start):
        # Manhattan distance (if no diagonal moves)
        return abs(start[0] - node[0]) + abs(start[1] - node[1])

    def calc_node(self, coords):
        h = self.calc_h(coords, self.dest)
        g = self.calc_g(coords, self.start_coords)
        return g, h

    def calc_surrounding_nodes(self):
        self.available_nodes = []
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            check_coords = [self.current_coords[0] - dx, self.current_coords[1] - dy]
            if self.map.get_num(check_coords[0], check_coords[1]) == 0: # Open
                # Only make the last coord unavailable
                if check_coords != self.last_coords:
                    g, h = self.calc_node(check_coords)
                    self.available_nodes.append([check_coords, g, h])

    def get_next_coord(self):
        next_coord = self.current_coords
        self.calc_surrounding_nodes()

        if not self.available_nodes:
            return next_coord  # No moves available

        coords = []
        gs = []
        hs = []
        fs = []

        for tup in self.available_nodes:
            coords.append(tup[0])
            gs.append(tup[1])
            hs.append(tup[2])
            fs.append(tup[1] + tup[2])
        
        lowest_f = min(fs)
        lowest_f_indexes = [i for i, f in enumerate(fs) if f == lowest_f]
        
        if len(lowest_f_indexes) == 1:
            selected_i = lowest_f_indexes[0]
        else:
            lowest_h = min([hs[i] for i in lowest_f_indexes])
            lowest_h_indexes = [i for i in lowest_f_indexes if hs[i] == lowest_h]
            selected_i = lowest_h_indexes[0]
        
        next_coord = coords[selected_i]
        self.last_coords = self.current_coords  # Update last coordinate
        self.current_coords = next_coord
        return next_coord