import pygame, sys, map, pathfinder

pygame.init()
pygame.font.init()

class Game:
    def __init__(self):
        self.display = pygame.display.set_mode([1280, 720])
        self.clock = pygame.time.Clock()
        self.framerate = 60
        self.map = map.Map()
        self.start = None
        self.destination = None
        self.pathfinder = pathfinder.Pathfinder([0, 0], [0, 0], self.map)
        self.font = pygame.font.Font(None, 16)
        self.path = []
        self.path_index = 0

    def poll(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.start is None:
                        self.destination = self.map.get_rect(event.pos)[1]
                        self.pathfinder.dest = self.destination
                    elif self.start is not None:
                        # Find path only if both start and destination are set
                        self.pathfinder.start_coords = self.start
                        self.pathfinder.dest = self.destination
                        self.path = self.pathfinder.find_path()

                        self.path_index = 0
                if event.button == 3:
                    if self.start is None:
                        self.start = self.map.get_rect(event.pos)[1]
                        self.pathfinder.start_coords = self.start

    def update(self):
        if self.path and self.path_index < len(self.path):
            self.pathfinder.current_coords = list(self.path[self.path_index])
            self.path_index += 1
        elif self.path == []:
            # No path found, optionally show a message or reset
            print("No path found!")

    def draw(self, surf):
        surf.fill([0, 0, 0])
        surf.blit(self.map.surf, [0, 0])
        if self.start is not None: 
            pygame.draw.rect(surf, [255, 0, 0], [self.start[0] * self.map.tile_size, self.start[1] * self.map.tile_size,
                                             self.map.tile_size, self.map.tile_size])
        if self.destination is not None: 
            pygame.draw.rect(surf, [0, 255, 0], [self.destination[0] * self.map.tile_size, self.destination[1] * self.map.tile_size,
                                                                          self.map.tile_size, self.map.tile_size])
        # Draw the path in yellow
        for coord in self.path:
            c = coord[0] * self.map.tile_size, coord[1] * self.map.tile_size
            pygame.draw.rect(surf, [255, 255, 0], [c[0], c[1], self.map.tile_size, self.map.tile_size])

        pygame.display.update()
        self.clock.tick(self.framerate)

game = Game()
while True:
    game.poll()
    game.update()
    game.draw(game.display)