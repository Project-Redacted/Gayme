import pygame as pg
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from object_handler import *
from pathfinding import *

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.level = spawn
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.pathfinding = PathFinding(self)
    
    def update(self):
        self.map.update(self.level)
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        if DEBUG_MODE:
            pg.display.set_caption(f"Garbage Game - FPS: {self.clock.get_fps() : 0.2f} - Delta Time: {self.delta_time / 1000 : 0.2f}")
        else:
            pg.display.set_caption(f"Garbage Game")
        
    def draw(self):
        if DEBUG_MODE:
            self.screen.fill('black')
            self.map.draw()
            self.player.draw()
        else:
            pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))
            pg.draw.rect(self.screen, ROOF_COLOR, (0, 0, WIDTH, HALF_HEIGHT))
            self.object_renderer.draw()
        
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
                
            if event.type == pg.KEYDOWN and event.key == pg.K_r:
                if self.level == spawn:
                    self.level = spawn_unlocked
                else:
                    self.level = spawn
    
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            
if __name__ == '__main__':
    game = Game()
    game.run()