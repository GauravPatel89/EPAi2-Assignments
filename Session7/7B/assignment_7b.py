import math

class Polygon:
    def __init__(self,num_vertices,circum_radius):
        '''
        This is a constructor for Polygon class (Regular Strictly convex Polygons). It takes as input number of vertices
        of the polygon and its circum radius. It calculates and makes available properties like interior angle,edge length,
        apothem, area and perimeter of the polygon.
        Input:
            num_vertices: int
            circum_radius: float
        '''
        self.num_vertices = num_vertices
        self.circum_radius = circum_radius
        self.interior_angle = (num_vertices - 2)*180.0/num_vertices 
        self.edge_length = 2.0 * circum_radius * math.sin(math.pi/num_vertices)
        self.apothem = circum_radius * math.cos(math.pi/num_vertices)
        self.area = 0.5 * self.num_vertices * self.edge_length * self.apothem
        self.perimeter = self.num_vertices*self.edge_length

    def __str__(self):
        '''
        Prepares a description for object of Polygon class.
        
        Input:
            None
        
        Return:
            str
        
        '''
        return f'Polygon: n = {self.num_vertices}, R = {self.circum_radius}\nInterior angle = {self.interior_angle}, Area = {self.area}'  
        

    def __repr__(self):
        '''
        Prepares a representation for object of Polygon class such that using it object can be reproduced.
        
        Input:
            None
        
        Return:
            str
        
        '''
        rep = f'Polygon(num_vertices={self.num_vertices},circum_radius={self.circum_radius})'
        return rep

    def __eq__(self,other):
        '''
        Compares current object with other object based on number of vertices and circum radius to decide whether both objects are equal.
        
        Input:
            other: Object of type Polygon
        
        Return:
            bool
        
        '''
        return((self.num_vertices==other.num_vertices) and (self.circum_radius == other.circum_radius))

    def __gt__(self, other):
        '''
        Compares current object with other object based on number of vertices to decide whether current object is greater than other object.
        
        Input:
            other: Object of type Polygon
        
        Return:
            bool
        
        '''
        if isinstance(other, Polygon):
            return self.num_vertices > other.num_vertices
        else:
            return False  

from functools import reduce
class Polygon_sequence:

    def __init__(self,max_num_vertices,circum_radius):
        '''
        This is a constructor for Polygon_sequence class. This class builds custom sequence of Polygon objects. It takes as input maximum number of vertices
        of the polygon and its circum radius. It then prepares a sequence of Polygons ranging from triangle (3 vertices) to Polygon with vertices maximum selected by the user.
        
        Input:
            max_num_vertices: int
            circum_radius: float
        '''
        self.max_num_vertices = max_num_vertices
        self.circum_radius = circum_radius
        self.polygon_list = [Polygon(n,self.circum_radius) for n in range(3,max_num_vertices+1)]
        self.max_efficiency_polygon = reduce(lambda a,b: a if (a.area/a.perimeter) > (b.area/b.perimeter) else b,self.polygon_list)

    def __getitem__(self, s):
        '''
        This function is implicitly used for iterating over our custom sequence. It returns single Polygon object or a list of it based
        on input parameter (int or a slice).
        
        Input:
            s: int or slice
        
        Return
            Polygon object or list of Polygon objects.
        '''
        if isinstance(s, int):
            if s < 0 or s > self.max_num_vertices - 3:
                raise IndexError
            return self.polygon_list[s]
        else:
            idx = s.indices(self.max_num_vertices - 3)
            rng = range(idx[0], idx[1], idx[2])
            return [self.polygon_list[n] for n in rng]

    def __len__(self):
        '''
        This function is implicitly called by len() function. It returns length of Polygon sequence.
        
        Return
            length: int
        '''
        return len(self.polygon_list)

    def __str__(self):
        '''
        This function is implicitly called by print() function. It returns short description of the object when it is printed.
        
        Return
            str
        '''
        return f'Polygon_sequence: [Polygon with vertices = 3 to vertices = {self.max_num_vertices} and Circum radius = {self.circum_radius}]'  

    def __repr__(self):
        '''
        This function returns representation of the object of this class such that the object can be reproduced using this representation.
        
        Return:
            str
        '''
        rep = f'Polygon_sequence(max_num_vertices={self.max_num_vertices},circum_radius={self.circum_radius})'
        return rep     
