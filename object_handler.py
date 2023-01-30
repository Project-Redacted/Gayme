from sprite_object import *
from npc import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.animated_sprite_path = 'resources/sprites/animated_sprites/'
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}
        
        # Sprite Map
        #add_sprite(SpriteObject(game))
        #add_sprite(AnimatedSprite(game))
        #add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(14.5, 5.5)))
        #add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(14.5, 7.5)))
        #add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(12.5, 7.5)))
        #add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(9.5, 7.5)))
        #add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(14.5, 12.5)))
        #add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(9.5, 20.5)))
        #add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(10.5, 20.5)))
        #add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(3.5, 14.5)))
        #add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(3.5, 18.5)))
        
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'boob.png', pos=(5, 4), scale=0.75, shift=-0.2))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'boob.png', pos=(8, 4), scale=0.75, shift=-0.2))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'boob.png', pos=(5, 16), scale=0.75, shift=-0.2))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'boob.png', pos=(8, 16), scale=0.75, shift=-0.2))
        
        
        # NPC Map
        #add_npc(NPC(game))
        add_npc(NPC(game, path=self.npc_sprite_path + 'peter-griffin/0.png', pos=(5, 18), scale=0.6, shift=0.38))
        
        
    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
    
    def add_npc(self, npc):
        self.npc_list.append(npc)
        
    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)