class Cylinder:

    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.pi * self.radius**2 * self.height

    def surface_area(self):
        return (2 * self.pi) * self.radius * self.height + (2 * self.pi) * (self.radius)**2


cyl = Cylinder()
print(cyl.volume())
print(cyl.surface_area())