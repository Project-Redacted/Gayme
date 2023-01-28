from settings import *
import pygame as pg
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ROT
        
    def movement(self):
        # Initialize variables
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        player_speed = PLAYER_SPEED * self.game.delta_time
        player_speed_sin = player_speed * sin_a
        player_speed_cos = player_speed * cos_a
        
        # player movement
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += player_speed_cos
            dy += player_speed_sin
        if keys[pg.K_s]:
            dx -= player_speed_cos
            dy -= player_speed_sin
        if keys[pg.K_a]:
            dx += player_speed_sin
            dy -= player_speed_cos
        if keys[pg.K_d]:
            dx -= player_speed_sin
            dy += player_speed_cos
        
        # set player position
        self.check_collision(dx, dy)
        
        # player rotation with arrow keys
        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau # tau = 2 * pi
    
    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map
    
    def check_collision(self, dx, dy):
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy
    
    def draw(self):
        pg.draw.line(self.game.screen, 'green', (self.x * 100, self.y * 100),
                     (self.x * 100 + WIDTH * math.cos(self.angle),
                      self.y * 100 + WIDTH * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'red', (self.x * 100, self.y * 100), 15)
    
    def mouse_control(self):
        mx, my = pg.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_SPEED, min(MOUSE_MAX_SPEED, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time
    
    def update(self):
        self.movement()
        #self.mouse_control()
        
    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)