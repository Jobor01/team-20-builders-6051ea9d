from levelup.position import position
class Character:
    name = ""
    map = None
    psoition = None

    def __init__(self, character_name):
        self.name = character_name if character_name != "" else "Builders"
        self.position = position(0,0)

    def enter_map(self, m):
        self.map = m
    
    def move(self, direction):
        return direction
    
        
