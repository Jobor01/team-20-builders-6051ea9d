import math
from dataclasses import dataclass
from levelup.position import position
from typing import List

@dataclass
class gamemap:
    num_position: int = 100
    position: List[List[position]] = None

    def __post_init__(self):
        grid_size = int(math.sqrt(self.num_position))
        self.position = [[position(x,y) for x in range(grid_size)]for y in range(grid_size)] 