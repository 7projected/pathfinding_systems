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

    def poll(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.destination == None: 
                        self.destination = self.map.get_rect(event.pos)[1]
                        self.pathfinder.dest = self.destination
                    else:
                        self.pathfinder.current_coords = self.pathfinder.get_next_coord()
                
                if event.button == 3:
                    if self.start == None:
                        self.start = self.map.get_rect(event.pos)[1]
                        self.pathfinder.start_coords = self.start
                        self.pathfinder.current_coords = self.start


    def update(self):
        pass

    def draw(self, surf):
        surf.fill([0, 0, 0])
        surf.blit(self.map.surf, [0, 0])
        if self.start != None: 
            pygame.draw.rect(surf, [255, 0, 0], [self.start[0] * self.map.tile_size, self.start[1] * self.map.tile_size,
                                             self.map.tile_size, self.map.tile_size])
        if self.destination != None: 
            pygame.draw.rect(surf, [0, 255, 0], [self.destination[0] * self.map.tile_size, self.destination[1] * self.map.tile_size,
                                                                          self.map.tile_size, self.map.tile_size])
        
        for arg in self.pathfinder.available_nodes:
            coords = arg[0]
            g = arg[1]
            h = arg[2]
            c = coords[0] * self.map.tile_size, coords[1] * self.map.tile_size
            pygame.draw.rect(surf, [255, 255, 0], [c[0], c[1], self.map.tile_size, self.map.tile_size])
            
            g_txt = self.font.render(f'g {g}', False, [0, 0, 0])
            h_txt = self.font.render(f'h {h}', False, [0, 0, 0])
            f_txt = self.font.render(f'f {h+g}', False, [0, 0, 0])
            surf.blit(g_txt, c)
            surf.blit(h_txt, [c[0], c[1] + 16])
            surf.blit(f_txt, [c[0], c[1] + 32])

        pygame.display.update()
        self.clock.tick(self.framerate)

game = Game()
while True:
    game.poll()
    game.update()
    game.draw(game.display)