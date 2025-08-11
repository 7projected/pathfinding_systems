import pygame, random, math

class Map:
    def __init__(self):
        self.map = []
        self.tile_size = 32

        self.tiles = 256

        self.rows = math.sqrt(self.tiles)
        for i in  range(self.tiles):
            rng = random.randint(0, 10)
            if rng == 1:
                self.map.append(1) # occpuied
            else:
                self.map.append(0)
        self.surf = pygame.Surface([self.rows * self.tile_size, self.rows * self.tile_size])
        self.rects = []
        self.redraw()

    def get_num(self, x, y):
        index = x + (y * self.rows)
        return self.map[int(index)]

    def get_rect(self, pos):
        pos_rect = pygame.Rect(pos[0], pos[1], 1 ,1)
        
        for t in self.rects:
            rect = t[0]
            coords = t[1]

            if pos_rect.colliderect(rect):
                return t

    def redraw(self):
        self.surf.fill([0, 0, 0])
        for i, num in enumerate(self.map):
            row = int(i / self.rows)
            x = i - (row * self.rows)
            if num == 0:
                self.rects.append([pygame.Rect(x * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size), [x, row]])
                col = [255, 255, 255]
            else:
                col = [0, 0, 0]

            pygame.draw.rect(self.surf, col, [x * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size])