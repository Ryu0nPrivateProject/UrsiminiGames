from ursina import *


class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model = 'sphere'
        self.collider = 'sphere'
        self.color = color.red
        self.position = Vec3(0, 5, 0)
        self.scale_x = 0.5
        self.scale_y = 0.5

        # custom fields
        self.moving_speed = 0.01
        self.velocity_x = Vec3(0, 0, 0)
        self.velocity_y = Vec3(0, 0, 0)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        r = held_keys['d'] * time.dt
        l = held_keys['a'] * time.dt
        self.velocity_x.x = r - l
        self.position += self.velocity_x
        print(self.velocity_x)
        print(self.position)

        hit_info = self.intersects()
        intersection_objects = hit_info.entities

        if len(intersection_objects) < 1:
            self.velocity_y.y -= time.dt * self.moving_speed
            self.position += self.velocity_y

        else:
            force = abs(self.velocity_y.y)
            self.velocity_y.y = 0
            self.velocity_y.y += force
            self.position += self.velocity_y
