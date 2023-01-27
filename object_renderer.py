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
        self.draw_background()
        self.render_game_objects()
        
    def draw_background(self):
        # Sky
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
        self.screen.blit(self.sky_texture, (-self.sky_offset, 0))
        self.screen.blit(self.sky_texture, (-self.sky_offset + WIDTH, 0))
        # Ground
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))
        
    def render_game_objects(self):
        list_objects = self.game.raycasting.objects_to_render
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
            1: self.get_texture('resources/textures/1.png'),
            2: self.get_texture('resources/textures/2.png'),
            3: self.get_texture('resources/textures/3.png'),
            4: self.get_texture('resources/textures/4.jpg'),
            5: self.get_texture('resources/textures/1.jpg'),
        }