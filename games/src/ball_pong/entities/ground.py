from ursina import *


class Ground(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model = 'cube'
        self.collider = 'box'
        self.color = color.white
        self.x = 0
        self.y = -1
        self.z = 0
        self.scale_x = 2
        self.scale_y = 0.5

        # custom fields
        self.moving_speed = 5
        self.vec_x = Vec3()
        self.vec_y = Vec3()

        for key, value in kwargs.items():
            setattr(self, key, value)
