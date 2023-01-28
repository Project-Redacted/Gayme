import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sounds/'
        #self.sound_type = pg.mixer.Sound(self.path + 'sound_type.extention')
        
        # Then to call the sound use
        # self.sound_type.play()