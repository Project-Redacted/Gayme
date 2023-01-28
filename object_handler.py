from sprite_object import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.animated_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        
        # Sprite Map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(14.5, 5.5)))
        add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(14.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(12.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(9.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(14.5, 12.5)))
        add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(9.5, 20.5)))
        add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(10.5, 20.5)))
        add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(3.5, 14.5)))
        add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(3.5, 18.5)))
        
    def update(self):
        [sprite.update() for sprite in self.sprite_list]
        
    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)