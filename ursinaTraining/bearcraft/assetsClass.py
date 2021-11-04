from ursina import *

class assetsCall:
    def call(self):
        self.grass_texture = load_texture('assets/grass_block.png')
        self.stone_texture = load_texture('assets/stone_block.png')
        self.brick_texture = load_texture('assets/brick_block.png')
        self.dirt_texture = load_texture('assets/dirt_block.png')
        self.sky_texture = load_texture('assets/skybox.png')
        self.arm_texture = load_texture('assets/arm_texture')
        self.punch_sound = Audio('assets/punch_sound', loop = False, autoplay = False)
        