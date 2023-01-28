import pygame as pg
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_texture = self.get_texture('resources/textures/sky.png', (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0
        
    def draw(self):
        #self.draw_background()
        self.render_game_objects()
        
    def draw_background(self):
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))
        pg.draw.rect(self.screen, ROOF_COLOR, (0, 0, WIDTH, HALF_HEIGHT))
        
    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            colour = [255 / (1 + depth ** 3.2 * 0.0002)] * 3
            image.fill(colour, special_flags=pg.BLEND_MULT)
            self.screen.blit(image, pos)
        
    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        texture = pg.transform.scale(texture, res)
        return texture
    
    def load_wall_textures(self):
        return {
            1: self.get_texture('resources/textures/bg.jpg'),
            2: self.get_texture('resources/textures/bg.jpg'),
            3: self.get_texture('resources/textures/bg.jpg'),
            4: self.get_texture('resources/textures/bg.jpg'),
            5: self.get_texture('resources/textures/bg.jpg'),
        }