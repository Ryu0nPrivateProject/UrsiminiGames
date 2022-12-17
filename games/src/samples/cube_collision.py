import numpy as np
from ursina import *

app = Ursina()
camera = EditorCamera()


class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model = 'cube'
        self.collider = 'box'
        self.color = color.red
        self.z = 0
        self.scale_x = 0.25
        self.scale_y = 0.25

        # custom fields
        self.moving_speed = 5
        self.vec_x = Vec3()
        self.vec_y = Vec3()

        for key, value in kwargs.items():
            setattr(self, key, value)

    def input(self, key):
        if key == 'space':
            self.animate_x(2, duration=1)

    def update(self):
        camera.position = Vec3(self.x, self.y, self.z)

        u = held_keys['w'] * time.dt * self.moving_speed
        d = held_keys['s'] * time.dt * self.moving_speed
        r = held_keys['d'] * time.dt * self.moving_speed
        l = held_keys['a'] * time.dt * self.moving_speed

        self.vec_x.x = r - l
        self.vec_y.y = u - d

        self.position += self.vec_x
        self.position += self.vec_y

        print(self.vec_x)
        print(self.vec_y, '\n')


class Obstacle(Entity):
    def __init__(self):
        super().__init__()
        self.model = 'cube'
        self.collider = 'box'
        self.collision = True
        self.color = color.blue
        self.z = 0
        self.scale_x = 0.5
        self.scale_y = 0.5

        # custom fields
        distribute_rate = 2.0
        self.x = np.random.randn() * distribute_rate
        self.y = np.random.randn() * distribute_rate

    def update(self):
        hit_info = self.intersects()
        intersected_objects = hit_info.entities
        intersected_player = list(filter(lambda object: isinstance(object, Player), intersected_objects))
        print(intersected_player)
        if intersected_player:
            intersected_player = intersected_player[0]
            self.x += intersected_player.vec_x.x
            self.y += intersected_player.vec_y.y


if __name__ == "__main__":
    player = Player(x=-1)
    num_obstacles = 10
    Obstacle = [Obstacle() for _ in range(num_obstacles)]
    app.run()
