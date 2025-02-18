class Shapes():
    def __init__(self, sides, name):
        self.sides = sides
        self.name = name
    def creating_lines(self):
        alpha = 360 / int(self.sides)
        for _ in range(self.sides):
            self.name.forward(150)
            self.name.right(alpha)