import math

class Polygon:
    def __init__(self,num_vertices,circum_radius):
        self.num_vertices = num_vertices
        self.circum_radius = circum_radius
        self.interior_angle = (num_vertices - 2)*180.0/num_vertices 
        self.edge_length = 2.0 * circum_radius * math.sin(math.pi/num_vertices)
        self.apothem = circum_radius * math.cos(math.pi/num_vertices)
        self.area = 0.5 * self.num_vertices * self.edge_length * self.apothem
        self.perimeter = self.num_vertices*self.edge_length

    def __str__(self):
        return f'Polygon: n = {self.num_vertices}, R = {self.circum_radius}\nInterior angle = {self.interior_angle}, Area = {self.area}'  


    def __repr__(self):
        rep = f'Polygon(num_vertices={self.num_vertices},circum_radius={self.circum_radius})'
        return rep

    def __eq__(self,other):
        return((self.num_vertices==other.num_vertices) and (self.circum_radius == other.circum_radius))

    def __gt__(self, other):
        if isinstance(other, Polygon):
            return self.num_vertices > other.num_vertices
        else:
            return False  