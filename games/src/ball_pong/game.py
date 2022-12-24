import numpy as np
from ursina import *
from entities.player import Player
from entities.ground import Ground, JumpingUpGround

app = Ursina()

camera = EditorCamera()
player = Player(camera=camera)
init_ground = Ground(x=0, y=0)
num_grounds = 100
grounds = [
    JumpingUpGround(
        x=np.random.randn()*5,
        y=(i+1)*4
    )
    for i, _ in enumerate(list(range(num_grounds)))
]

app.run()
