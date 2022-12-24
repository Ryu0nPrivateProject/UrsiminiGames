from ursina import *


class Ground(Entity):
    def __init__(self, x: float, y: float, **kwargs):
        super().__init__()
        self.model = 'cube'
        self.collider = 'box'
        self.color = color.white
        self.x = x
        self.y = y
        self.z = 0
        self.scale_x = 2
        self.scale_y = 0.5

        # custom fields
        self.moving_speed = 5
        self.vec_x = Vec3()
        self.vec_y = Vec3()
        self.viscosity = 1.2  # ratio that jumping more (1.0 ~ 1.8)

        for key, value in kwargs.items():
            setattr(self, key, value)


class JumpingUpGround(Entity):
    def __init__(self, x: float, y: float, **kwargs):
        super().__init__()
        self.model = 'cube'
        self.collider = 'box'
        self.color = color.yellow
        self.x = x
        self.y = y
        self.z = 0
        self.scale_x = 2
        self.scale_y = 0.5

        # custom fields
        self.moving_speed = 5
        self.vec_x = Vec3()
        self.vec_y = Vec3()
        self.viscosity = 1.5  # ratio that jumping more (1.0 ~ 1.8)

        for key, value in kwargs.items():
            setattr(self, key, value)
