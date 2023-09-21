class Character:
    name = ""

    def __init__(self, character_name):
        self.name = character_name if character_name != "" else "Builders"
    
    def enter_map(self, m):
        self.map = m
        
