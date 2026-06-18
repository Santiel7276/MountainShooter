class Entity:
    def __init__(self):
        self.name: str = ""
        self.surf: Surface = None
        self.rect: Rect = None

    def move(self) -> None:
        pass