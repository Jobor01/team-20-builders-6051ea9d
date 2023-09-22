import math
from dataclasses import dataclass
from levelup.position import position
from typing import List

@dataclass
class gamemap:
    num_position: int = 100
    position: List[List[position]] = None

    def __post_init__(self):
        self.grid_size = int(math.sqrt(self.num_position))
        self.position = [[position(x,y) for x in range(0, self.grid_size)]for y in range(0, self.grid_size)]
        print(self.grid_size)

    def calculate_position(self, startpos, movement):
        if movement == 'n':
            return self.position[startpos.y + 1 if startpos.y < (self.grid_size - 1) else startpos.y][startpos.x]
        elif movement == 's':
            return self.position[startpos.y - 1 if startpos.y > 0 else startpos.y][startpos.x]
        elif movement == 'e':
             return self.position[startpos.y][startpos.x + 1 if startpos.x < (self.grid_size - 1) else startpos.x]
        elif movement == 'w':
            return self.position[startpos.y][startpos.x - 1 if startpos.x > 0 else startpos.x]
        else :
            return self.position[startpos.y][startpos.x]
            
