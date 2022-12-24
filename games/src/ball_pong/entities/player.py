from ursina import *


class Player(Entity):
    def __init__(self, camera: EditorCamera, **kwargs):
        super().__init__()
        self.model = 'sphere'
        self.collider = 'sphere'
        self.color = color.red
        self.position = Vec3(0, 3, 0)
        self.scale_x = 0.5
        self.scale_y = 0.5

        # custom fields
        self.camera = camera
        self.moving_speed_x = 0.2
        self.moving_speed_y = 0.05
        self.velocity_x = Vec3(0, 0, 0)
        self.velocity_y = Vec3(0, 0, 0)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        r = held_keys['d'] * time.dt
        l = held_keys['a'] * time.dt
        self.velocity_x.x += r - l
        self.position += self.velocity_x * self.moving_speed_x

        hit_info = self.intersects()
        intersection_objects = hit_info.entities

        if len(intersection_objects) < 1:
            self.velocity_y.y -= time.dt * self.moving_speed_y

        else:
            # When collision is occur
            intersection_object = intersection_objects[0]
            force = abs(self.velocity_y.y) * intersection_object.viscosity

            if self.velocity_y.y < 0:
                # hit the upper surface of ground
                self.velocity_y.y = 0
                self.velocity_y.y += force
            else:
                self.velocity_y.y = 0
                force_reduction = abs(1.0 - intersection_object.viscosity) + 0.1
                self.velocity_y.y -= force * (1.0 - force_reduction)

        self.position += self.velocity_y
        self.camera.position = self.position
